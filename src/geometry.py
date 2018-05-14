"""
geometry
"""


from fractions import Fraction
import math
import typing as tp


Number = tp.Union[int, float, complex, Fraction]


class Point:
    """Represents a Point in 2D and 3D space. (for 2D, z=0)
    Also represents a Position Vector, anchored at origin,
    or a Vertex of a polygon or a polyhedron.
    """

    def __init__(self, x: Number =0, y: Number =0, z: Number =0) -> None:
        """
        :param x: a Number representing the x coordinate
        :param y: a Number representing the y coordinate
        :param z: a Number representing the z coordinate
        Point() returns a Point at origin
        """

        self._point = [x, y, z]

    def __len__(self):
        return len(self._point)

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @property
    def z(self):
        try:
            return self[2]
        except IndexError:
            return 0

    @x.setter
    def x(self, value: Number):
        self[0] = value

    @y.setter
    def y(self, value: Number):
        self[1] = value

    @z.setter
    def z(self, value: Number):
        self[2] = value

    def __getitem__(self, key):
        if key > len(self):
            raise IndexError
        return self._point[key]

    def __setitem__(self, key, value: Number):
        if key > len(self):
            raise IndexError
        self._point[key] = value

    def __iter__(self) -> tp.Iterator:
        return iter(self._point)

    def __hash__(self) -> int:
        return hash((tuple(self._point)))

    def __eq__(self, other: 'Point') -> bool:
        return all(math.isclose(selfv, otherv) for selfv, otherv in zip(self, other))

    def __add__(self, other: 'Point') -> 'Point':
        return self.__class__(*(selfv + otherv for selfv, otherv in zip(self, other)))

    def __iadd__(self, other: 'Point') -> 'Point':
        """making sure attributes set on self remain"""
        for idx in range(len(self)):
            self[idx] += other[idx]
        return self

    def __sub__(self, other: 'Point') -> 'Point':
        return self.__class__(*(selfv - otherv for selfv, otherv in zip(self, other)))

    def __isub__(self, other: 'Point') -> 'Point':
        """making sure attributes set on self remain"""
        for idx in range(len(self)):
            self[idx] -= other[idx]
        return self

    def __mul__(self, factor: Number) -> 'Point':
        return self.__class__(*(val * factor for val in self))

    def __rmul__(self, factor: Number) -> 'Point':
        return self * factor

    def __imul__(self, factor: Number) -> 'Point':
        """making sure attributes set on self remain"""
        for idx in range(len(self)):
            self[idx] *= factor
        return self

    def __floordiv__(self, divisor: Number) -> 'Point':
        assert divisor != 0, 'divisor must not be zero'
        return self.__class__(*(val // divisor for val in self))

    def __ifloordiv__(self, divisor: Number) -> 'Point':
        """making sure attributes set on self remain"""
        assert divisor != 0, 'divisor must not be zero'
        for idx in range(len(self)):
            self[idx] //= divisor
        return self

    def __truediv__(self, divisor: Number) -> 'Point':
        assert divisor != 0, 'divisor must not be zero'
        return self.__class__(*(val / divisor for val in self))

    def __itruediv__(self, divisor: Number) -> 'Point':
        """making sure attributes set on self remain"""
        assert divisor != 0, 'divisor must not be zero'
        for idx in range(len(self)):
            self[idx] /= divisor
        return self

    def __neg__(self) -> 'Point':
        """making sure attributes set on self remain"""
        for idx in range(len(self)):
            self[idx] = -self[idx]
        return self

    def __abs__(self) -> 'Point':
        """making sure attributes set on self remain"""
        for idx in range(len(self)):
            self[idx] = abs(self[idx])
        return self

    def __complex__(self) -> complex:
        assert self.z == 0, 'z is not zero, cannot cast to Complex'
        return complex(self.x, self.y)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({', '.join(str(v) for v in self)})"

    def __repr__(self) -> str:
        return str(self)

    def copy(self):
        return self.__class__(*self._point)

    def scale(self, factor: Number) -> None:
        """mutates the Point, returns None"""
        for idx in range(len(self)):
            self[idx] *= factor

    def distance_from_point(self, other: 'Point') -> Number:
        """if both points are not the same dimension, the extra dimensions
        are dropped - i/e an orthogonal projection of the largest dimensional
        object is used
        """
        return math.sqrt(sum((selfv - otherv)**2 for selfv, otherv in zip(self, other)))

    def mid_point(self, other: 'Point') -> 'Point':
        return self.__class__(*((selfv + otherv) / 2 for selfv, otherv in zip(self, other)))


class Point2D(Point):
    """specific subclass to allow use with habitual GUI that take a two-Tuple
    coordinates; ex Turtle.goto(coord) - coord is a two-Tuple like object
    """

    def __init__(self, x: Number =0, y: Number =0) -> None:
        """
        :param x: a Number representing the x coordinate
        :param y: a Number representing the y coordinate
        Point2D() returns a Point at origin
        """
        super().__init__(x=x, y=y)
        self._point = [x, y]

    def rotate(self, theta):
        return Point2D(self.x * math.cos(theta) - self.y * math.sin(theta),
                       self.y * math.cos(theta) + self.x * math.sin(theta))


class LineSegment:
    """Represents a LineSegment
    Also represents an Edge of a polygon or a polyhedron.
    """

    def __init__(self, start: 'Point', end: 'Point'):
        self.start = start
        self.end = end
        self._segment = [self.start, self.end]


class NumberPlane:
    """
    The two unit vectors e1 and e2 are defined at origin.
    they must be scaled to be displayed
    """

    def __init__(self, e1: Point2D, e2: Point2D, num_rows: int=20, num_cols: int=20)-> None:
        """
        :param e1: a vector at origin defining unit length in one direction
        :param e2: a vector at origin defining unit length in one direction
        :param width: the number of graduations to display from left to right
        :param height: the number of graduations to display from top to bottom
        e1 and e2 are not necessarily orthogonal
        Origin is centered
        """
        self.e1: Point2D = e1
        self.e2: Point2D = e2
        self.num_rows = num_rows
        self.num_cols = num_rows

        self.grid = []    # collection of line segments representing the grid lines
        self.points = []  # collection of intersection points between grid lines
        self.make_grid()

    def get_point(self, x: Number, y: Number):
        return x * self.e1 + y * self.e2

    def make_grid(self):
        columns_low = []
        columns_high = []
        for row in range(-self.num_rows, self.num_rows, 1):
            this_row = []
            for col in range(-self.num_cols, self.num_cols, 1):
                this_row.append(row * self.e2 + col * self.e1 )
                if row == -self.num_rows:
                    columns_low.append(this_row[-1])
                if row == self.num_rows - 1:
                    columns_high.append(this_row[-1])
            self.points += this_row
            self.grid.append(LineSegment(this_row[0], this_row[-1]))
        for low_start, high_end in zip(columns_low, columns_high):
            self.grid.append(LineSegment(low_start, high_end))


if __name__ == '__main__':

    p3 = Point(1, 2, 3)
    p2 = Point2D(1, 2)
    print(p3, len(p3), p2, len(p2))

    import tkinter as tk

    WIDTH = 800
    HEIGHT = 800

    def make_point():
        """creates a Point in Model coordinates from values
        obtained in canvas coordinates"""


    class App(tk.Frame):
        def __init__(self, parent):
            super().__init__(parent)
            self.parent = parent
            self.canvas = tk.Canvas(self.parent, width=WIDTH, height=HEIGHT)

            self.quit_btn = tk.Button(parent, text='Quit', command=self.quit)
            self.quit_btn.pack()

            self.capture_segment_btn = tk.Button(self.parent,
                                                 text='segment',
                                                 command=lambda cmd=self.capture_segment:
                                                 self.bind_click_on_canvas(cmd))
            self.capture_segment_btn.pack()

            self.capture_point_btn = tk.Button(self.parent,
                                               text='point',
                                               command=lambda cmd=self.capture_point:
                                               self.bind_click_on_canvas(cmd))
            self.capture_point_btn.pack()

            self.canvas.pack()

            self.pack()

            self.points = []
            self.segments = []
            self.segment_start_point = None

            # add a NumberPlane
            e1, e2 = Point2D(2, 1/6), Point2D(-1, 3)
            self.plane = NumberPlane(e1, e2)
            self.draw_plane()

        def to_pixel_coordinates(self, point):
            origin_in_frame: Point2D = Point2D(WIDTH // 2, HEIGHT // 2)
            frame_origin: Point2D = Point2D(0, HEIGHT)   # <-- flip to origin at bottom left
            scale: int = 20
            p = origin_in_frame + scale * point
            p.y = -p.y                                   # <-- reflection over x axis (e1)
            return p + frame_origin

        def draw_plane(self):
            origin = self.plane.get_point(0, 0)
            right1up1 = self.plane.get_point(1, 1)
            ox, oy = self.to_pixel_coordinates(origin)
            self.canvas.create_oval(ox - 4, oy - 4, ox + 4, oy + 4, fill='red')
            rux, ruy = self.to_pixel_coordinates(right1up1)
            self.canvas.create_oval(rux - 4, ruy - 4, rux + 4, ruy + 4, fill='blue')

            # draw points on grid
            for point in self.plane.points:
                x, y = self.to_pixel_coordinates(point)

                self.canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill='grey80')

            # draw grid
            for segment in self.plane.grid:
                self.canvas.create_line(*self.to_pixel_coordinates(segment.start),
                                        *self.to_pixel_coordinates(segment.end),
                                        fill='grey80', dash=(4, 3))

            # draw unit vectors e1 and e2
            self.canvas.create_line(*self.to_pixel_coordinates(Point(0, 0)),
                                    *self.to_pixel_coordinates(self.plane.e1),
                                    width=3, fill='blue', arrow=tk.LAST)
            self.canvas.create_line(*self.to_pixel_coordinates(Point(0, 0)),
                                    *self.to_pixel_coordinates(self.plane.e2),
                                    width=3, fill='red', arrow=tk.LAST)

        def bind_click_on_canvas(self, cmd):
            self.canvas.bind('<1>', cmd)

        def capture_segment(self, event):
            x, y = event.x, event.y
            if self.segment_start_point:
                self.segments.append(LineSegment(Point2D(*self.segment_start_point), Point2D(x, y)))
                self.segment_start_point = None
            else:
                self.segment_start_point = (x, y)
            self.draw()

        def capture_point(self, event):
            x, y = event.x, event.y
            self.points.append(Point(x, y, z=0))
            self.draw()

        def draw(self):
            self.canvas.delete('all')
            self.draw_plane()
            for point in self.points:
                x, y, z = point
                self.canvas.create_oval(x-3, y-3, x+3, y+3, fill='black')

            for segment in self.segments:
                self.canvas.create_line(*segment.start, *segment.end, fill='black')


    root = tk.Tk()
    app = App(root)
    root.mainloop()
