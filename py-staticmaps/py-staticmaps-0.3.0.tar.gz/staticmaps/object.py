# py-staticmaps
# Copyright (c) 2020 Florian Pigorsch; see /LICENSE for licensing information

from abc import ABC, abstractmethod
import typing

import s2sphere  # type: ignore

from .svg_renderer import SvgRenderer
from .cairo_renderer import CairoRenderer
from .transformer import Transformer


PixelBoundsT = typing.Tuple[int, int, int, int]


class Object(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def extra_pixel_bounds(self) -> PixelBoundsT:
        return 0, 0, 0, 0

    @abstractmethod
    def bounds(self) -> s2sphere.LatLngRect:
        return s2sphere.LatLngRect()

    def render_svg(self, renderer: SvgRenderer) -> None:
        # pylint: disable=unused-argument
        t = "SVG"
        c = type(self).__name__
        m = "render_svg"
        raise RuntimeError(f"Cannot render to {t} since the class '{c}' doesn't implement the '{m}' method.")

    def render_cairo(self, renderer: CairoRenderer) -> None:
        # pylint: disable=unused-argument
        t = "Cairo"
        c = type(self).__name__
        m = "render_cairo"
        raise RuntimeError(f"Cannot render to {t} since the class '{c}' doesn't implement the '{m}' method.")

    def pixel_rect(self, trans: Transformer) -> typing.Tuple[float, float, float, float]:
        """Return the pixel rect (left, top, right, bottom) of the object when using the supplied Transformer."""
        bounds = self.bounds()
        se_x, se_y = trans.ll2pixel(bounds.get_vertex(1))
        nw_x, nw_y = trans.ll2pixel(bounds.get_vertex(3))
        l, t, r, b = self.extra_pixel_bounds()
        return nw_x - l, nw_y - t, se_x + r, se_y + b
