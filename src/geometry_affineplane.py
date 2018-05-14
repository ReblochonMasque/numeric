from src.geometry import Point2D, LineSegment
import tkinter as tk
from tkinter import ttk


class CoordinateSystem:
    """
    Tree like structure for representing coordinate systems and converting back and forth
    between them.
    Each child unit vectors are expressed wrt the parent
    """

    E1 = Point2D(1, 0)
    E2 = Point2D(0, 1)

    def __init__(self, e1: Point2D, e2: Point2D, parent: 'CoordinateSystem'=None, name=''):
        """
        :param e1: Unit vector e1 in this coordinate system wrt parent coordinate system
        :param e2: Unit vector e2 in this coordinate system wrt parent coordinate system
        :param parent: parent coordinate system - if None --> root
        :param name: The name of this coordinate system
        """

        # objects must be scaled and oriented in the

        self.parent = parent
        self.e1 = e1
        self.e2 = e2
        self.name = name


class AffineGrid:   # subclass of a 'elements to draw container / data structure'
    """a set of unit vectors and an associated grid
    """

    WIDTH = 500  # in pixels
    HEIGHT = 500  # in pixels
    ORIGIN = Point2D(WIDTH // 2, HEIGHT // 2)

    def __init__(self, e1: Point2D, e2: Point2D):
        self.e1: Point2D = e1
        self.e2: Point2D = e2
        self.grid_lines = []   # a collection of line segments
        self.make_grid_lines()

    def make_grid_lines(self):   # the grid extends 10 units in every direction
        """
        trace a large number of multiples of e1 & e2 in all directions
        trace lines
        """
        e1_lines = []
        for y in range(-10, 11):
            e1_lines.append(LineSegment(start=self.position(Point2D(-10, y)),
                                        end=self.position(Point2D(10, y))))
        e2_lines = []
        for x in range(-10, 11):
            e2_lines.append(LineSegment(start=self.position(Point2D(x, -10)),
                                        end=self.position(Point2D(x, 10))))
        self.grid_lines = [e1_lines, e2_lines]

    def position(self, point: Point2D) -> Point2D:
        a, b = self.e1.x, self.e1.y    # e1_lands_at.x, e1_lands_at.y
        c, d = self.e2.x, self.e2.y    # e2_lands_at.x, e2_lands_at.y
        x, y = point.x, point.y
        landed_at = Point2D(a * x + c * y, b * x + d * y)
        landed_at.y = - landed_at.y
        return landed_at + AffineGrid.ORIGIN


def transform_from_world_to_canvas_coordinates(e1_lands_at: Point2D, e2_lands_at: Point2D, point: Point2D):
    """
    takes a collection of world elements and place them on the canvas
    """
    a, b = e1_lands_at.x, e1_lands_at.y
    c, d = e2_lands_at.x, e2_lands_at.y
    x, y = point.x, point.y
    return Point2D(a * x + c * y, b * x + d * y)


class TransformFromCanvasToWorldCoordinates:
    """
    takes elements in canvas coordinates (from canvas event coordinates, maybe?)
    and transforms them into world coordinates
    """


class TransformFromModelToWorldCoordinates:
    """
    takes elements in model coordinates (from canvas event coordinates, maybe?)
    and places them into the world coordinates
    """


class AffinePlane(tk.Canvas):
    """
    """

    WIDTH = 500    # in pixels
    HEIGHT = 500   # in pixels
    ORIGIN = Point2D(WIDTH//2, HEIGHT//2)
    E1 = Point2D(1, 0)
    E2 = Point2D(0, 1)

    def __init__(self, parent, **kwargs):
        self.parent = parent
        super().__init__(self.parent, **kwargs)

        self.e1 = Point2D(20, 5)
        self.e2 = Point2D(3, 15)

        self.grid = AffineGrid(self.e1, self.e2)
        self.draw_grid()

        self.bind('<Motion>', self.mouse_move)

    def mouse_move(self, event):
        x, y = event.x, event.y
        print(x, y)

    def draw_grid(self):
        for axis in self.grid.grid_lines:
            for line in axis:
                self.create_line(*line.start, *line.end, fill='grey60', dash=(4, 3))

        # draw unit vectors e1 and e2
        self.create_line(*AffinePlane.ORIGIN, *self.grid.position(AffinePlane.E1), width=3, fill='blue', arrow=tk.LAST)
        self.create_line(*AffinePlane.ORIGIN, *self.grid.position(AffinePlane.E2), width=3, fill='red', arrow=tk.LAST)


if __name__ == '__main__':

    class App(ttk.Frame):

        def __init__(self, master):
            self.master = master
            super().__init__(master)
            self.plane = AffinePlane(self.master, width=500, height=500)
            self.plane.pack()
            # self.plane['bg'] = 'cyan'
            # self.plane.create_line(-100, -100, 100, 100)
            self.pack()

    root = tk.Tk()
    App(root)
    root.mainloop()
