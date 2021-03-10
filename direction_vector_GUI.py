"""
from javidx9/splines
small example of direction vector display on canvas
press mouse button and move to see the direction vector
"""

import tkinter as tk
from collections import deque

from src import Vector2D as Vector
from src import Point2D as Point


def draw_direction_vector(canvas, anchor: Point, vec: Vector, _vid=[None]) -> None:
    """draws and updates the scaled normalized direction vector
    on the canvas.
    Keeps track of the id of the canvas item last drawn
    """
    if _vid[0] is not None:
        canvas.delete(_vid[0])
    normed_scaled_v = vec * 50
    end_point = anchor + normed_scaled_v
    _vid[0] = canvas.create_line(*anchor, *end_point, arrow=tk.LAST)


_maxlen = 4


def direction(event, _direct=deque([Point(0, 0) for _ in range(_maxlen)],
                                   maxlen=_maxlen)) -> None:
    """stores the previous position, and uses it to calculate the direction
    from the current position.
    updates these variables
    """
    _direct.append(Point(event.x, event.y))
    p0, _, _, p1 = _direct  # skipping 2 points smoothens the movement a bit
    draw_direction_vector(canvas, p1, (p1 - p0).unit())


if __name__ == '__main__':

    root = tk.Tk()
    canvas = tk.Canvas(root, bg='cyan')
    canvas.pack()
    canvas.bind('<B1-Motion>', direction)
    root.mainloop()
