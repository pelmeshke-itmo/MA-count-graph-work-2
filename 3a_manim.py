import math

from manim import *
from manim import config as global_config

global_config.background_color = GRAY_B
global_config.pixel_width = global_config.pixel_height


class MyScene(Scene):
    def construct(self):
        side = 7
        color = PURPLE
        second_color = BLUE_D
        side_color = DARK_BROWN
        font_size = 130
        stroke_width = 30

        s = Square(side, color=color, stroke_width=stroke_width, fill_color=second_color, fill_opacity=0.2)
        s.add(Tex('$S$', color=BLUE_D, font_size=font_size))
        side_object = Line((RIGHT + DOWN) * 1.046 * side / 2, (RIGHT + UP) * 1.046 * side / 2, color=side_color,
                           stroke_width=stroke_width).next_to(s, RIGHT, buff=0)
        s.add(Tex('$P$', color=color, font_size=font_size).next_to(s, DOWN * 2))
        self.add(s, side_object)
        self.add(Tex('$a$', color=side_color, font_size=font_size).next_to(side_object, RIGHT * 2))
