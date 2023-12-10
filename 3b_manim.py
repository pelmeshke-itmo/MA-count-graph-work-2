import math

from manim import *
from manim import config as global_config

global_config.background_color = GRAY_B
global_config.pixel_width = global_config.pixel_height

class MyScene(Scene):
    def construct(self):
        radius = 5
        color = PURPLE
        second_color = BLUE_D
        angle_color = LIGHT_PINK
        radius_color = TEAL_E
        font_size = 130
        stroke_width = 30
        second_stroke_width = 15
        angle = -140 / 180 * math.pi

        d = Dot(ORIGIN, 0.16, color=color)

        r1 = Line(ORIGIN, UP * radius * 1.03, color=color, stroke_width=stroke_width)
        r2 = Line(ORIGIN, 1.03 * radius * (UP * math.sin(angle + math.pi / 2) + RIGHT * math.cos(angle + math.pi / 2)),
                  color=color, stroke_width=stroke_width)

        arc = Arc(radius, math.pi / 2, angle, color=color, stroke_width=stroke_width)
        arc2 = Arc(radius, angle - math.pi / 2, 5 / 2 * math.pi - angle, color=second_color,
                         stroke_width=second_stroke_width)

        angle_arc = Arc(1, math.pi / 2, angle, color=angle_color, stroke_width=second_stroke_width / 2)
        r1_ = Line(ORIGIN, UP * radius * 1.03, color=radius_color, stroke_width=stroke_width)
        phi = Tex(r'$\varphi$', color=angle_color, font_size=font_size).next_to(angle_arc, RIGHT * 2)
        r1_text = Tex(r'$r$', color=radius_color, font_size=font_size).next_to(r1, LEFT * 2)
        arc_text = Tex('$L$', color=color, font_size=font_size).next_to(arc, RIGHT * 2)

        sector = Sector(radius, 0, color=second_color, fill_opacity=0.2, start_angle=math.pi / 2, angle=angle)
        sector.add(Tex('$S$', color=BLUE_D, font_size=font_size).move_to(sector).shift(UP * 1.5))
        self.add(sector)
        self.add(angle_arc, phi, r1_text, arc_text, sector)

        self.add(arc2)
        self.add(d, arc, r1, r2, r1_)
