import math
from numeric.src.geometry import Point2D
import turtle


def perp(p1, p2):
    """returns the ccw perpendicular vector of same length"""
    v = p2-p1
    v_perp = Point2D(-v.y, v.x)
    return v_perp


class DragonCurve:

    def __init__(self, level=4):
        self.start = Point2D(0, -1)
        self.end = Point2D(0, 1)
        self.points = [self.start, self.end]
        for _ in range(level):
            self.fold()

    def fold(self):
        new_points = []
        new_origin = self.points[-1]
        for p in self.points:
            to_origin = new_origin - p
            rotated =  Point2D(-to_origin.y, to_origin.x) + new_origin
            new_points.append(rotated)
        self.points += new_points[::-1]


class KochCurve:

    def __init__(self, level=4):
        self.start = Point2D(-1/2, math.sqrt(3)/2)
        self.end = Point2D(1/2, math.sqrt(3)/2)
        self.points = [(self.start,
                        self.end,
                        Point2D(1, 0),
                        Point2D(1/2, -math.sqrt(3)/2),
                        Point2D(-1/2, -math.sqrt(3)/2),
                        Point2D(-1, 0),
                        self.start)]
        for _ in range(level):
            self.iterate()

    def iterate(self):
        previous_step = self.points[-1]
        next_step_points = [previous_step[0]]
        for p0, p4 in zip(previous_step[: -1], previous_step[1:]):
            p1 = p0 + (p4-p0) / 3
            p3 = p0 + 2 * (p4-p0) / 3

            perpendicular = perp(p1, p3)
            mid = p0.mid_point(p4)
            p2 = mid + perpendicular * math.sqrt(3) / 2
            next_step_points += [p1, p2, p3, p4]

        self.points.append(tuple(next_step_points))


if __name__ == '__main__':

    k = KochCurve(level=7)
    print('done')

    screen = turtle.Turtle().screen
    origin = Point2D(0, 0)
    scaling_to_sreen = 500

    t = turtle.Turtle()
    t.penup()
    t.goto(k.points[-1][0] * scaling_to_sreen + origin)

    for point in k.points[-1]:
        t.pendown()
        t.goto(point * scaling_to_sreen + origin)

    screen.mainloop()

    # dragon = DragonCurve(level=15)
    # print('done')
    #
    # screen = turtle.Turtle().screen
    # screen.clear()
    #
    # origin = Point2D(0, 0)
    # scaling_to_sreen = 2
    #
    # t = turtle.Turtle()
    # t.speed(1)
    # t.hideturtle()
    # t.penup()
    # t.goto(dragon.points[0] * scaling_to_sreen + origin)
    #
    # for point in dragon.points:
    #     t.pendown()
    #     t.goto((point * scaling_to_sreen) + origin)
    #
    # t.hideturtle()
    # t.clearstamps()
    #
    # screen.mainloop()

