from rlgym.utils.obs_builders import ObsBuilder
from rlgym.utils import common_values, math
import numpy as np


class RhobotObs(ObsBuilder):
    def __init__(self):
        super().__init__()
        self.obs_size = 66

    def reset(self, optional_data=None):
        pass

    def build_obs(self, state, optional_data=None):
        raise NotImplementedError

    def build_obs_for_player(self, player, state, prev_action, optional_data=None) -> np.ndarray:
        if prev_action is None:
            print("ATTEMPTED TO BUILD RHOBOT OBS WITH NO PREV ACTIONS ARGUMENT!")
            raise AssertionError

        players = state.players
        if player.team_num == common_values.ORANGE_TEAM:
            player_car = player.inverted_car_data
            ball = state.inv_ball
        else:
            player_car = player.car_data
            ball = state.ball

        ob = []
        ob.append(prev_action)
        ob.append([int(player.has_flip),
                   int(player.boost_amount),
                   int(player.on_ground)])


        ob.append(player_car.position)
        ob.append(player_car.orientation)
        ob.append(np.sin(player_car.orientation))
        ob.append(np.cos(player_car.orientation))
        yaw = player_car.orientation[2]
        angle_between_bot_and_target = np.arctan2(ball.position[1] - player_car.position[1],
                                                  ball.position[0] - player_car.position[0])
        
        angle_front_to_target = angle_between_bot_and_target - yaw
        ob.append([angle_front_to_target])
        ob.append(player_car.linear_velocity)
        ob.append(player_car.angular_velocity)

        ob.append(ball.position)
        ob.append(ball.linear_velocity)
        ob.append(ball.angular_velocity)

        ob.append(common_values.ORANGE_GOAL_CENTER)
        ob.append(common_values.BLUE_GOAL_CENTER)

        pb_dist = math.vecmag(math.get_dist(player_car.position, ball.position))
        ob.append([pb_dist])

        # FIXME this only works for the blue team
        pg_dist = math.vecmag(math.get_dist(player_car.position, common_values.ORANGE_GOAL_CENTER))
        ob.append([pg_dist])

        # FIXME this only works for the blue team
        pog_dist = math.vecmag(math.get_dist(player_car.position, common_values.BLUE_GOAL_CENTER))
        ob.append([pog_dist])

        for other in players:
            if other.car_id == player.car_id:
                continue

            if other.team_num == common_values.BLUE_TEAM and player.team_num == other.team_num:
                car_data = other.car_data
            else:
                car_data = other.inverted_car_data

            # TODO: COMMENT THIS OUT
            #car_data = ObsBuilder.get_random_physics_state()

            ob.append(car_data.position)
            ob.append(car_data.orientation)
            ob.append(np.sin(car_data.orientation))
            ob.append(np.cos(car_data.orientation))
            ob.append(car_data.linear_velocity)
            ob.append(car_data.angular_velocity)

            pc_dist = math.vecmag(math.get_dist(player_car.position, car_data.position))
            ob.append([pc_dist])

        return np.concatenate(ob)
