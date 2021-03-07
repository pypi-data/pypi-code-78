import copy
import math
import os
import random
import re
import threading
from datetime import datetime
from typing import Dict, List, Optional, Union

from kivy.clock import Clock

from katrain.core.constants import (
    OUTPUT_DEBUG,
    OUTPUT_EXTRA_DEBUG,
    OUTPUT_INFO,
    PLAYER_AI,
    PLAYER_HUMAN,
    PROGRAM_NAME,
    SGF_INTERNAL_COMMENTS_MARKER,
    STATUS_ANALYSIS,
    STATUS_ERROR,
    STATUS_INFO,
    STATUS_TEACHING,
)
from katrain.core.engine import KataGoEngine
from katrain.core.game_node import GameNode
from katrain.core.lang import i18n, rank_label
from katrain.core.sgf_parser import SGF, Move
from katrain.core.utils import var_to_grid, weighted_selection_without_replacement


class IllegalMoveException(Exception):
    pass


class KaTrainSGF(SGF):
    _NODE_CLASS = GameNode


class BaseGame:
    """Represents a game of go, including an implementation of capture rules."""

    DEFAULT_PROPERTIES = {"GM": 1, "FF": 4}

    def __init__(
        self,
        katrain,
        move_tree: GameNode = None,
        game_properties: Optional[Dict] = None,
        sgf_filename=None,
    ):
        self.katrain = katrain
        self._lock = threading.Lock()
        self.game_id = datetime.strftime(datetime.now(), "%Y-%m-%d %H %M %S")
        self.sgf_filename = sgf_filename

        self.insert_mode = False
        self.external_game = False  # not generated by katrain at some point
        if move_tree:
            self.root = move_tree
            self.external_game = PROGRAM_NAME not in self.root.get_property("AP", "")
            self.komi = self.root.komi
            handicap = int(self.root.handicap)
            num_starting_moves_black = 0
            node = self.root
            while node.children:
                node = node.children[0]
                if node.player == "B":
                    num_starting_moves_black += 1
                else:
                    break

            if (
                handicap >= 2
                and not self.root.placements
                and not (num_starting_moves_black == handicap)
                and not (self.root.children and self.root.children[0].placements)
            ):  # not really according to sgf, and not sure if still needed, last clause for fox
                self.root.place_handicap_stones(handicap)
        else:
            board_size = katrain.config("game/size")
            rules = katrain.config("game/rules")
            self.komi = katrain.config("game/komi")
            self.root = GameNode(
                properties={
                    **Game.DEFAULT_PROPERTIES,
                    **{"SZ": board_size, "KM": self.komi, "DT": self.game_id, "RU": rules},
                    **(game_properties or {}),
                }
            )
            handicap = katrain.config("game/handicap")
            if handicap:
                self.root.place_handicap_stones(handicap)

        if not self.root.get_property("RU"):
            self.root.set_property("RU", katrain.config("game/rules"))

        self.set_current_node(self.root)
        self.main_time_used = 0

        # restore shortcuts
        shortcut_id_to_node = {node.get_property("KTSID", None): node for node in self.root.nodes_in_tree}
        for node in self.root.nodes_in_tree:
            shortcut_id = node.get_property("KTSF", None)
            if shortcut_id and shortcut_id in shortcut_id_to_node:
                shortcut_id_to_node[shortcut_id].add_shortcut(node)

    # -- move tree functions --
    def _init_state(self):
        board_size_x, board_size_y = self.board_size
        self.board = [
            [-1 for _x in range(board_size_x)] for _y in range(board_size_y)
        ]  # type: List[List[int]]  #  board pos -> chain id
        self.chains = []  # type: List[List[Move]]  #   chain id -> chain
        self.prisoners = []  # type: List[Move]
        self.last_capture = []  # type: List[Move]

    def _calculate_groups(self):
        with self._lock:
            self._init_state()
            try:
                for node in self.current_node.nodes_from_root:
                    for m in node.move_with_placements:
                        self._validate_move_and_update_chains(
                            m, True
                        )  # ignore ko since we didn't know if it was forced
                    if node.clear_placements:  # handle AE by playing all moves left from empty board
                        clear_coords = {c.coords for c in node.clear_placements}
                        stones = [m for c in self.chains for m in c if m.coords not in clear_coords]
                        self._init_state()
                        for m in stones:
                            self._validate_move_and_update_chains(m, True)
            except IllegalMoveException as e:
                raise Exception(f"Unexpected illegal move ({str(e)})")

    def _validate_move_and_update_chains(self, move: Move, ignore_ko: bool):
        board_size_x, board_size_y = self.board_size

        def neighbours(moves):
            return {
                self.board[m.coords[1] + dy][m.coords[0] + dx]
                for m in moves
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                if 0 <= m.coords[0] + dx < board_size_x and 0 <= m.coords[1] + dy < board_size_y
            }

        ko_or_snapback = len(self.last_capture) == 1 and self.last_capture[0] == move
        self.last_capture = []

        if move.is_pass:
            return

        if self.board[move.coords[1]][move.coords[0]] != -1:
            raise IllegalMoveException("Space occupied")

        nb_chains = list({c for c in neighbours([move]) if c >= 0 and self.chains[c][0].player == move.player})
        if nb_chains:
            this_chain = nb_chains[0]
            self.board = [
                [nb_chains[0] if sq in nb_chains else sq for sq in line] for line in self.board
            ]  # merge chains connected by this move
            for oc in nb_chains[1:]:
                self.chains[nb_chains[0]] += self.chains[oc]
                self.chains[oc] = []
            self.chains[nb_chains[0]].append(move)
        else:
            this_chain = len(self.chains)
            self.chains.append([move])
        self.board[move.coords[1]][move.coords[0]] = this_chain

        opp_nb_chains = {c for c in neighbours([move]) if c >= 0 and self.chains[c][0].player != move.player}
        for c in opp_nb_chains:
            if -1 not in neighbours(self.chains[c]):
                self.last_capture += self.chains[c]
                for om in self.chains[c]:
                    self.board[om.coords[1]][om.coords[0]] = -1
                self.chains[c] = []
        if ko_or_snapback and len(self.last_capture) == 1 and not ignore_ko:
            raise IllegalMoveException("Ko")
        self.prisoners += self.last_capture

        if -1 not in neighbours(self.chains[this_chain]):  # TODO: NZ rules?
            raise IllegalMoveException("Suicide")

    # Play a Move from the current position, raise IllegalMoveException if invalid.
    def play(self, move: Move, ignore_ko: bool = False):
        board_size_x, board_size_y = self.board_size
        if not move.is_pass and not (0 <= move.coords[0] < board_size_x and 0 <= move.coords[1] < board_size_y):
            raise IllegalMoveException(f"Move {move} outside of board coordinates")
        try:
            self._validate_move_and_update_chains(move, ignore_ko)
        except IllegalMoveException:
            self._calculate_groups()
            raise
        with self._lock:
            played_node = self.current_node.play(move)
            self.current_node = played_node
        return played_node

    # Insert a list of moves from root, often just adding one.
    def sync_branch(self, moves: List[Move]):
        node = self.root
        with self._lock:
            for move in moves:
                node = node.play(move)
        return node

    def set_current_node(self, node):
        self.current_node = node
        self._calculate_groups()

    def undo(self, n_times=1, stop_on_mistake=None):
        break_on_branch = False
        cn = self.current_node  # avoid race conditions
        break_on_main_branch = False
        last_branching_node = cn
        if n_times == "branch":
            n_times = 9999
            break_on_branch = True
        elif n_times == "main-branch":
            n_times = 9999
            break_on_main_branch = True
        for move in range(n_times):
            if (
                stop_on_mistake is not None
                and cn.points_lost is not None
                and cn.points_lost >= stop_on_mistake
                and self.katrain.players_info[cn.player].player_type != PLAYER_AI
            ):
                self.set_current_node(cn.parent)
                return
            previous_cn = cn
            if cn.shortcut_from:
                cn = cn.shortcut_from
            elif not cn.is_root:
                cn = cn.parent
            else:
                break  # root
            if break_on_branch and len(cn.children) > 1:
                break
            elif break_on_main_branch and cn.ordered_children[0] != previous_cn:  # implies > 1 child
                last_branching_node = cn
        if break_on_main_branch:
            cn = last_branching_node
        if cn is not self.current_node:
            self.set_current_node(cn)

    def redo(self, n_times=1, stop_on_mistake=None):
        cn = self.current_node  # avoid race conditions
        for move in range(n_times):
            if cn.children:
                child = cn.ordered_children[0]
                shortcut_to = [m for m, v in cn.shortcuts_to if child == v]  # are we about to go to a shortcut node?
                if shortcut_to:
                    child = shortcut_to[0]
                cn = child
            if (
                move > 0
                and stop_on_mistake is not None
                and cn.points_lost is not None
                and cn.points_lost >= stop_on_mistake
                and self.katrain.players_info[cn.player].player_type != PLAYER_AI
            ):
                self.set_current_node(cn.parent)
                return
        if stop_on_mistake is None:
            self.set_current_node(cn)

    @property
    def board_size(self):
        return self.root.board_size

    @property
    def stones(self):
        with self._lock:
            return sum(self.chains, [])

    @property
    def end_result(self):
        if self.current_node.end_state:
            return self.current_node.end_state
        if self.current_node.parent and self.current_node.is_pass and self.current_node.parent.is_pass:
            return self.manual_score or i18n._("board-game-end")

    @property
    def prisoner_count(
        self,
    ) -> Dict:  # returns prisoners that are of a certain colour as {B: black stones captures, W: white stones captures}
        return {player: sum([m.player == player for m in self.prisoners]) for player in Move.PLAYERS}

    @property
    def rules(self):
        return self.root.ruleset

    @property
    def manual_score(self):
        rules = self.rules
        if (
            not self.current_node.ownership
            or str(rules).lower() not in ["jp", "japanese"]
            or not self.current_node.parent
            or not self.current_node.parent.ownership
        ):
            if not self.current_node.score:
                return None
            return self.current_node.format_score(round(2 * self.current_node.score) / 2) + "?"
        board_size_x, board_size_y = self.board_size
        mean_ownership = [(c + p) / 2 for c, p in zip(self.current_node.ownership, self.current_node.parent.ownership)]
        ownership_grid = var_to_grid(mean_ownership, (board_size_x, board_size_y))
        stones = {m.coords: m.player for m in self.stones}
        lo_threshold = 0.15
        hi_threshold = 0.85
        max_unknown = 10
        max_dame = 4 * (board_size_x + board_size_y)

        def japanese_score_square(square, owner):
            player = stones.get(square, None)
            if (
                (player == "B" and owner > hi_threshold)
                or (player == "W" and owner < -hi_threshold)
                or abs(owner) < lo_threshold
            ):
                return 0  # dame or own stones
            if player is None and abs(owner) >= hi_threshold:
                return round(owner)  # surrounded empty intersection
            if (player == "B" and owner < -hi_threshold) or (player == "W" and owner > hi_threshold):
                return 2 * round(owner)  # captured stone
            return math.nan  # unknown!

        scored_squares = [
            japanese_score_square((x, y), ownership_grid[y][x])
            for y in range(board_size_y)
            for x in range(board_size_x)
        ]
        num_sq = {t: sum([s == t for s in scored_squares]) for t in [-2, -1, 0, 1, 2]}
        num_unkn = sum(math.isnan(s) for s in scored_squares)
        prisoners = self.prisoner_count
        score = sum([t * n for t, n in num_sq.items()]) + prisoners["W"] - prisoners["B"] - self.komi
        self.katrain.log(
            f"Manual Scoring: {num_sq} score by square with {num_unkn} unknown, {prisoners} captures, and {self.komi} komi -> score = {score}",
            OUTPUT_DEBUG,
        )
        if num_unkn > max_unknown or (num_sq[0] - len(stones)) > max_dame:
            return None
        return self.current_node.format_score(score)

    def __repr__(self):
        return (
            "\n".join("".join(self.chains[c][0].player if c >= 0 else "-" for c in line) for line in self.board)
            + f"\ncaptures: {self.prisoner_count}"
        )

    def update_root_properties(self):
        def player_name(player_info):
            if player_info.name and player_info.player_type == PLAYER_HUMAN:
                return player_info.name
            else:
                return f"{i18n._(player_info.player_type)} ({i18n._(player_info.player_subtype)}){SGF_INTERNAL_COMMENTS_MARKER}"

        root_properties = self.root.properties
        x_properties = {}
        for bw in "BW":
            if not self.external_game:
                x_properties["P" + bw] = player_name(self.katrain.players_info[bw])
                player_info = self.katrain.players_info[bw]
                if player_info.player_type == PLAYER_AI:
                    x_properties[bw + "R"] = rank_label(player_info.calculated_rank)
        if "+" in str(self.end_result):
            x_properties["RE"] = self.end_result
        self.root.properties = {**root_properties, **{k: [v] for k, v in x_properties.items()}}

    def generate_filename(self):
        self.update_root_properties()
        player_names = {
            bw: re.sub(r"[\u200b\u3164'<>:\"/\\|?*]", "", self.root.get_property("P" + bw, bw)) for bw in "BW"
        }
        base_game_name = f"{PROGRAM_NAME}_{player_names['B']} vs {player_names['W']}"
        return f"{base_game_name} {self.game_id}.sgf"

    def write_sgf(self, filename: str, trainer_config: Optional[Dict] = None):
        if trainer_config is None:
            trainer_config = self.katrain.config("trainer", {})
        save_feedback = trainer_config.get("save_feedback", False)
        eval_thresholds = trainer_config["eval_thresholds"]
        save_analysis = trainer_config.get("save_analysis", False)
        save_marks = trainer_config.get("save_marks", False)
        self.update_root_properties()
        show_dots_for = {
            bw: trainer_config.get("eval_show_ai", True) or self.katrain.players_info[bw].human for bw in "BW"
        }
        sgf = self.root.sgf(
            save_comments_player=show_dots_for,
            save_comments_class=save_feedback,
            eval_thresholds=eval_thresholds,
            save_analysis=save_analysis,
            save_marks=save_marks,
        )
        self.sgf_filename = filename
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(sgf)
        return i18n._("sgf written").format(file_name=filename)


class Game(BaseGame):
    """Extensions related to analysis etc."""

    def __init__(
        self,
        katrain,
        engine: Union[Dict, KataGoEngine],
        move_tree: GameNode = None,
        analyze_fast=False,
        game_properties: Optional[Dict] = None,
        sgf_filename=None,
    ):
        super().__init__(
            katrain=katrain, move_tree=move_tree, game_properties=game_properties, sgf_filename=sgf_filename
        )
        if not isinstance(engine, Dict):
            engine = {"B": engine, "W": engine}
        self.engines = engine

        self.insert_mode = False
        self.insert_after = None
        self.region_of_interest = None

        threading.Thread(
            target=lambda: self.analyze_all_nodes(-1_000_000, analyze_fast=analyze_fast, even_if_present=False),
            daemon=True,
        ).start()  # return faster, but bypass Kivy Clock

    def analyze_all_nodes(self, priority=0, analyze_fast=False, even_if_present=True):
        for node in self.root.nodes_in_tree:
            # forced, or not present, or something went wrong in loading
            if even_if_present or not node.analysis_from_sgf or not node.load_analysis():
                node.clear_analysis()
                node.analyze(self.engines[node.next_player], priority=priority, analyze_fast=analyze_fast)

    @property
    def rules(self):  # maybe not needed
        return self.engines["B"].get_rules(self.root)

    def set_current_node(self, node):
        if self.insert_mode:
            self.katrain.controls.set_status(i18n._("finish inserting before navigating"), STATUS_ERROR)
            return
        super().set_current_node(node)

    def undo(self, n_times=1, stop_on_mistake=None):
        if self.insert_mode:  # in insert mode, undo = delete
            cn = self.current_node  # avoid race conditions
            if n_times == 1 and cn not in self.insert_after.nodes_from_root:
                cn.parent.children = [c for c in cn.parent.children if c != cn]
                self.current_node = cn.parent
                self._calculate_groups()
            return
        super().undo(n_times=n_times, stop_on_mistake=stop_on_mistake)

    def reset_current_analysis(self):
        cn = self.current_node
        engine = self.engines[cn.next_player]
        engine.terminate_queries(cn)
        cn.clear_analysis()
        cn.analyze(engine)

    def redo(self, n_times=1, stop_on_mistake=None):
        if self.insert_mode:
            return
        super().redo(n_times=n_times, stop_on_mistake=stop_on_mistake)

    def set_insert_mode(self, mode):
        if mode == "toggle":
            mode = not self.insert_mode
        if mode == self.insert_mode:
            return
        self.insert_mode = mode
        if mode:
            children = self.current_node.ordered_children
            if not children:
                self.insert_mode = False
            else:
                self.insert_after = self.current_node.ordered_children[0]
                self.katrain.controls.set_status(i18n._("starting insert mode"), STATUS_INFO)
        else:
            copy_from_node = self.insert_after
            copy_to_node = self.current_node
            num_copied = 0
            if copy_to_node != self.insert_after.parent:
                above_insertion_root = self.insert_after.parent.nodes_from_root
                already_inserted_moves = [
                    n.move for n in copy_to_node.nodes_from_root if n not in above_insertion_root and n.move
                ]
                try:
                    while True:
                        if copy_from_node.move not in already_inserted_moves:
                            for m in copy_from_node.move_with_placements:
                                self._validate_move_and_update_chains(m, True)
                            # this inserts
                            copy_to_node = GameNode(
                                parent=copy_to_node, properties=copy.deepcopy(copy_from_node.properties)
                            )
                            num_copied += 1
                        if not copy_from_node.children:
                            break
                        copy_from_node = copy_from_node.ordered_children[0]
                except IllegalMoveException:
                    pass  # illegal move = stop
                self._calculate_groups()  # recalculate groups
                self.katrain.controls.set_status(
                    i18n._("ending insert mode").format(num_copied=num_copied), STATUS_INFO
                )
                self.analyze_all_nodes(analyze_fast=True, even_if_present=False)
            else:
                self.katrain.controls.set_status("", STATUS_INFO)
        self.katrain.controls.move_tree.insert_node = self.insert_after if self.insert_mode else None
        self.katrain.controls.move_tree.redraw()
        self.katrain.update_state(redraw_board=True)

    # Play a Move from the current position, raise IllegalMoveException if invalid.
    def play(self, move: Move, ignore_ko: bool = False, analyze=True):
        played_node = super().play(move, ignore_ko)
        if analyze:
            if self.region_of_interest:
                played_node.analyze(self.engines[played_node.next_player], analyze_fast=True)
                played_node.analyze(self.engines[played_node.next_player], region_of_interest=self.region_of_interest)
            else:
                played_node.analyze(self.engines[played_node.next_player])
        return played_node

    def set_region_of_interest(self, region_of_interest):
        x1, x2, y1, y2 = region_of_interest
        xmin, xmax = min(x1, x2), max(x1, x2)
        ymin, ymax = min(y1, y2), max(y1, y2)
        szx, szy = self.board_size
        if not (xmin == xmax and ymin == ymax) and not (xmax - xmin + 1 >= szx and ymax - ymin + 1 >= szy):
            self.region_of_interest = [xmin, xmax, ymin, ymax]
        else:
            self.region_of_interest = None
        self.katrain.controls.set_status("", OUTPUT_INFO)

    def analyze_extra(self, mode, **kwargs):
        stones = {s.coords for s in self.stones}
        cn = self.current_node

        if mode == "stop":
            for e in set(self.engines.values()):
                e.terminate_queries()
            self.katrain.idle_analysis = False
            return

        engine = self.engines[cn.next_player]
        Clock.schedule_once(self.katrain.analysis_controls.hints.activate, 0)

        if mode == "extra":
            if kwargs.get("continuous", False):
                visits = min(
                    1_000_000_000, max(engine.config["max_visits"], math.ceil(cn.analysis_visits_requested * 1.25))
                )
            else:
                visits = cn.analysis_visits_requested + engine.config["max_visits"]
                self.katrain.controls.set_status(i18n._("extra analysis").format(visits=visits), STATUS_ANALYSIS)
            self.katrain.controls.set_status(i18n._("extra analysis").format(visits=visits), STATUS_ANALYSIS)
            cn.analyze(
                engine, visits=visits, priority=-1_000, region_of_interest=self.region_of_interest, time_limit=False
            )
            return
        if mode == "game":
            nodes = self.root.nodes_in_tree
            if "visits" in kwargs:
                visits = kwargs["visits"]
            else:
                min_visits = min(node.analysis_visits_requested for node in nodes)
                visits = min_visits + engine.config["max_visits"]
            for node in nodes:
                node.analyze(engine, visits=visits, priority=-1_000_000, time_limit=False, report_every=None)
            self.katrain.controls.set_status(i18n._("game re-analysis").format(visits=visits), STATUS_ANALYSIS)
            return

        elif mode == "sweep":
            board_size_x, board_size_y = self.board_size

            if cn.analysis_exists:
                policy_grid = (
                    var_to_grid(self.current_node.policy, size=(board_size_x, board_size_y))
                    if self.current_node.policy
                    else None
                )
                analyze_moves = sorted(
                    [
                        Move(coords=(x, y), player=cn.next_player)
                        for x in range(board_size_x)
                        for y in range(board_size_y)
                        if (policy_grid is None and (x, y) not in stones) or policy_grid[y][x] >= 0
                    ],
                    key=lambda mv: -policy_grid[mv.coords[1]][mv.coords[0]],
                )
            else:
                analyze_moves = [
                    Move(coords=(x, y), player=cn.next_player)
                    for x in range(board_size_x)
                    for y in range(board_size_y)
                    if (x, y) not in stones
                ]
            visits = engine.config["fast_visits"]
            self.katrain.controls.set_status(i18n._("sweep analysis").format(visits=visits), STATUS_ANALYSIS)
            priority = -1_000_000_000
        elif mode in ["equalize", "alternative", "local"]:
            if not cn.analysis_complete and mode != "local":
                self.katrain.controls.set_status(i18n._("wait-before-extra-analysis"), STATUS_INFO, self.current_node)
                return
            if mode == "alternative":  # also do a quick update on current candidates so it doesn't look too weird
                self.katrain.controls.set_status(i18n._("alternative analysis"), STATUS_ANALYSIS)
                cn.analyze(engine, priority=-500, time_limit=False, find_alternatives="alternative")
                visits = engine.config["fast_visits"]
            else:  # equalize
                visits = max(d["visits"] for d in cn.analysis["moves"].values())
                self.katrain.controls.set_status(i18n._("equalizing analysis").format(visits=visits), STATUS_ANALYSIS)
            priority = -1_000
            analyze_moves = [Move.from_gtp(gtp, player=cn.next_player) for gtp, _ in cn.analysis["moves"].items()]
        else:
            raise ValueError("Invalid analysis mode")

        for move in analyze_moves:
            if cn.analysis["moves"].get(move.gtp(), {"visits": 0})["visits"] < visits:
                cn.analyze(
                    engine, priority=priority, visits=visits, refine_move=move, time_limit=False
                )  # explicitly requested so take as long as you need

    def selfplay(self, until_move, target_b_advantage=None):
        cn = self.current_node

        if target_b_advantage is not None:
            analysis_kwargs = {"visits": max(25, self.katrain.config("engine/fast_visits"))}
            engine_settings = {"wideRootNoise": 0.03}
        else:
            analysis_kwargs = engine_settings = {}

        def set_analysis(node, result):
            node.set_analysis(result)
            analyze_and_play(node)

        def request_analysis_for_node(node):
            self.engines[node.player].request_analysis(
                node,
                callback=lambda result, _partial: set_analysis(node, result),
                priority=-1000,
                analyze_fast=True,
                extra_settings=engine_settings,
                **analysis_kwargs,
            )

        def analyze_and_play(node):
            nonlocal cn, engine_settings
            candidates = node.candidate_moves
            if self.katrain.game is not self:
                return  # a new game happened
            ai_thoughts = "Move generated by AI self-play\n"
            if until_move != "end" and target_b_advantage is not None:  # setup pos
                if node.depth >= until_move or candidates[0]["move"] == "pass":
                    self.set_current_node(node)
                    return
                target_score = cn.score + (node.depth - cn.depth + 1) * (target_b_advantage - cn.score) / (
                    until_move - cn.depth
                )
                max_loss = 5
                stddev = min(3, 0.5 + (until_move - node.depth) * 0.15)
                ai_thoughts += f"Selecting moves aiming at score {target_score:.1f} +/- {stddev:.2f} with < {max_loss} points lost\n"
                if abs(node.score - target_score) < 3 * stddev:
                    weighted_cands = [
                        (
                            move,
                            math.exp(-0.5 * (abs(move["scoreLead"] - target_score) / stddev) ** 2)
                            * math.exp(-0.5 * (min(0, move["pointsLost"]) / max_loss) ** 2),
                        )
                        for i, move in enumerate(candidates)
                        if move["pointsLost"] < max_loss or i == 0
                    ]
                    move_info = weighted_selection_without_replacement(weighted_cands, 1)[0][0]
                    for move, wt in weighted_cands:
                        self.katrain.log(
                            f"{'* ' if move_info == move else '  '} {move['move']} {move['scoreLead']} {wt}",
                            OUTPUT_EXTRA_DEBUG,
                        )
                        ai_thoughts += f"Move option: {move['move']} score {move['scoreLead']:.2f} loss {move['pointsLost']:.2f} weight {wt:.3e}\n"
                else:  # we're a bit lost, far away from target, just push it closer
                    move_info = min(candidates, key=lambda move: abs(move["scoreLead"] - target_score))
                    self.katrain.log(
                        f"* Played {move_info['move']} {move_info['scoreLead']} because score deviation between current score {node.score} and target score {target_score} > {3*stddev}",
                        OUTPUT_EXTRA_DEBUG,
                    )
                    ai_thoughts += f"Move played to close difference between score {node.score:.1f} and target {target_score:.1f} quickly."

                self.katrain.log(
                    f"Self-play until {until_move} target {target_b_advantage}: {len(candidates)} candidates -> move {move_info['move']} score {move_info['scoreLead']} point loss {move_info['pointsLost']}",
                    OUTPUT_DEBUG,
                )
                move = Move.from_gtp(move_info["move"], player=node.next_player)
            elif candidates:  # just selfplay to end
                move = Move.from_gtp(candidates[0]["move"], player=node.next_player)
            else:  # 1 visit etc
                polmoves = node.policy_ranking
                move = polmoves[0][1] if polmoves else Move(None)
            if move.is_pass:
                if self.current_node == cn:
                    self.set_current_node(node)
                return
            new_node = GameNode(parent=node, move=move)
            new_node.ai_thoughts = ai_thoughts
            if until_move != "end" and target_b_advantage is not None:
                self.set_current_node(new_node)
                self.katrain.controls.set_status(
                    i18n._("setup game status message").format(move=new_node.depth, until_move=until_move),
                    STATUS_INFO,
                )
            else:
                if node != cn:
                    node.remove_shortcut()
                cn.add_shortcut(new_node)

            self.katrain.controls.move_tree.redraw_tree_trigger()
            request_analysis_for_node(new_node)

        request_analysis_for_node(cn)

    def analyze_undo(self, node):
        train_config = self.katrain.config("trainer")
        move = node.move
        if node != self.current_node or node.auto_undo is not None or not node.analysis_complete or not move:
            return
        points_lost = node.points_lost
        thresholds = train_config["eval_thresholds"]
        num_undo_prompts = train_config["num_undo_prompts"]
        i = 0
        while i < len(thresholds) and points_lost < thresholds[i]:
            i += 1
        num_undos = num_undo_prompts[i] if i < len(num_undo_prompts) else 0
        if num_undos == 0:
            undo = False
        elif num_undos < 1:  # probability
            undo = int(node.undo_threshold < num_undos) and len(node.parent.children) == 1
        else:
            undo = len(node.parent.children) <= num_undos

        node.auto_undo = undo
        if undo:
            self.undo(1)
            self.katrain.controls.set_status(
                i18n._("teaching undo message").format(move=move.gtp(), points_lost=points_lost), STATUS_TEACHING
            )
            self.katrain.update_state()
