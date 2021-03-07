from numeric.src.vector import Vector2D

import random
import tkinter as tk


class App(tk.Frame):

    def __init__(self, master, width=500, height=500):
        self.master = master
        super().__init__()
        self.canvas = tk.Canvas(self.master, width=width, height=height)
        self.origin = Vector2D(width//2, height//2)
        self.axis = AxisXY(self.canvas, width, height)
        self.vectors = []
        self.make_vectors()
        self.canvas.pack()

    def make_vectors(self):
        for _ in range(1000):
            v = Vector2D(x=random.randrange(-250, 250), y=random.randrange(-250, 250))
            self.vectors.append(Vector2Dtk(self.canvas, self.origin, v))


class AxisXY:

    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.start_x = height // 2, 0
        self.end_x = height // 2, width
        self.start_y = 0, width // 2
        self.end_y = height, width // 2

        canvas.create_line(*self.start_x, *self.end_x)
        canvas.create_line(*self.start_y, *self.end_y)


class Vector2Dtk:

    def __init__(self, canvas, anchor: Vector2D, vector: Vector2D):
        self.placed_vector = vector + anchor
        self.coord_x = self.placed_vector.x
        self.coord_y = self.placed_vector.y
        canvas.create_line(*anchor.v, *self.placed_vector.v)


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()


