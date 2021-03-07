from numeric.src.geometry import Point2D
import tkinter as tk


class Particle:

    def __init__(self, position: Point2D = Point2D(10, 10), velocity: Point2D = Point2D(0, 0)):
        self.pos = position
        self.vel = velocity
        self.attractor = Attractor()

    @property
    def x(self):
        return self.pos.x

    @property
    def y(self):
        return self.pos.y

    def update(self, acc: Point2D = Point2D(0, 0)):
        self.vel += self.attractor.get_acc(self)
        self.pos += self.vel

    def __str__(self):
        return f"Particle({self.pos}, {self.vel})"


class Attractor:

    def __init__(self, position: Point2D = Point2D(0, 0)):
        self.pos = position
        self.weight = 1

    def get_acc(self, p: Particle):

        x, y = p.x, p.y
        if x > 0 and y > 0:
            if x > 2 * y:
                return Point2D(-1, 0)
            if y > 2 * x:
                return Point2D(0, -1)
            else:
                return Point2D(-1, -1)

        if x < 0 and y > 0:
            if -x > 2 * y:
                return Point2D(1, 0)
            if y > 2 * -x:
                return Point2D(0, -1)
            else:
                return Point2D(1, -1)

        if x < 0 and y < 0:
            if -x > 2 * -y:
                return Point2D(1, 0)
            if -y > 2 * -x:
                return Point2D(0, 1)
            else:
                return Point2D(1, 1)

        if x > 0 and y < 0:
            if x > 2 * -y:
                return Point2D(-1, 0)
            if -y > 2 * -x:
                return Point2D(0, 1)
            else:
                return Point2D(-1, 1)

        return Point2D(0, 0)


if __name__ == '__main__':

    import turtle

    t = turtle.Turtle()
    scale = 2

    cut_off = 500

    # pos = Point2D(-8, 2) # velocity: Point2D = Point2D(1, 1)
    # pos = Point2D(4, 1) # velocity: Point2D = Point2D(0, 0)  infinitely expanding

    infinite_orbits = [Point2D(4, 1), Point2D(1, 4), Point2D(4, 18), Point2D(18, 4), Point2D(2, 9), Point2D(9, 2),
                       Point2D(3, 7), Point2D(7, 3), Point2D(5, 7), Point2D(7, 5), Point2D(6, 8), Point2D(8, 6),
                       Point2D(7, 9), Point2D(9, 7), Point2D(8, 13), Point2D(13, 8), Point2D(9, 14), Point2D(14, 9),
                       Point2D(11, 13), Point2D(13, 11),
                       Point2D(12, 14), Point2D(14, 12), Point2D(13, 18), Point2D(18, 13), Point2D(14, 16),
                       Point2D(16, 14), Point2D(15, 18), Point2D(18, 15), Point2D(16, 18), Point2D(18, 16),
                       Point2D(18, 20), Point2D(20, 18)]

    infinites = []

    for c in range(45, 51):
        for r in range(c, 51):
            pos = Point2D(c, r)
            if pos in infinite_orbits:
                continue
            particle = Particle(position=pos.copy(), velocity=Point2D(0, 0))
            print(particle)

            t.penup()
            t.goto(particle.pos * scale)
            t.pendown()

            dt = 0

            while True:
                dt += 1
                particle.update()
                t.goto(particle.pos * scale)
                # print(dt, particle)
                if (particle.pos == pos and particle.vel == Point2D(0, 0)) or dt > cut_off:
                    print(f'orbit: {particle}, {pos}', dt)
                    if dt > cut_off:
                        infinites.append(pos)
                        infinites.append(Point2D(pos.y, pos.x))
                    break

    print(infinites)


