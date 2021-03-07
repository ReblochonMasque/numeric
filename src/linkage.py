import time
from numeric.src.geometry import Point2D
import tkinter as tk


class Bone:

    def __init__(self):
        self.start = Point2D(0, 0)
        self.end = Point2D(10, 0)
        self.direction = Point2D(1, 0)
        self.joint = Joint(self.start, self.direction)

    def rotate(self):
        while True:
            print(self.start, self.end)
            self.joint.rotate()
            self.end = self.end.rotate(0.01)
            time.sleep(1)


class Joint:

    def __init__(self, pos: Point2D, direction):
        self.pos = pos
        self.direction = direction

    def rotate(self, dtheta=0.01):
        self.pos = self.pos.rotate(dtheta)
        self.direction = self.pos


class Skeleton:
    pass


if __name__ == '__main__':

    bone = Bone()
    bone.rotate()

