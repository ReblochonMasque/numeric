import math
import tkinter as tk

WIDTH, HEIGHT = 800, 800
ORIGIN = (0, 0)
CENTER = (WIDTH//2, HEIGHT//2)


class SymmetryVis(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.canvas = tk.Canvas(self.parent, width=WIDTH, height=HEIGHT, bg='cyan')
        self.canvas.pack()
        self.pack()

        self.shapes = shapes
        self.draw()

    def add_shape(self, shape):
        self.models.append(shape)

    def draw(self):
        for shape in self.shapes:
            print(f"drawing shapes: {shape}")
            self.canvas.create_polygon(shape.points, outline='black', fill=shape.color)


class Model:
    """2D polygon centered at origin"""

    def __init__(self, points):
        self.points = points[:]


class Shape:

    def __init__(self, model, position=CENTER, scaling_factor=1, rotation=None, color='blue'):
        self.model = model
        self.position = position
        self.scaling_factor = scaling_factor
        self.rotation = rotation
        self.angle = rotation
        self.points = None
        self.color = color
        self.place()

    def place(self):
        self.points = [list(point) for point in self.model.points]
        self.rotate()
        self.scale()
        self.translate()

    def scale(self):
        for point in self.points:
            point[0] *= self.scaling_factor
            point[1] *= self.scaling_factor

    def rotate(self):
        for point in self.points:
            p0 = point[0] * math.cos(self.angle) - point[1] * math.sin(self.angle)
            point[1] = point[0] * math.sin(self.angle) + point[1] * math.cos(self.angle)
            point[0] = p0

    def translate(self):
        for point in self.points:
            point[0] += self.position[0]
            point[1] += self.position[1]

    def draw(self, canvas):
        canvas.create_polygon(self.points)


if __name__ == '__main__':

    triangle_model = Model(((0.5, -math.sqrt(3)/6), (0, math.sqrt(3)/3), (-0.5, -math.sqrt(3)/6)))
    triangle_shape1 = Shape(triangle_model, position=CENTER, scaling_factor=50, rotation=0, color='red')
    triangle_shape2 = Shape(triangle_model, position=(WIDTH//2+50, HEIGHT//2), scaling_factor=50, rotation=math.pi/24, color='')

    sqrt3 = math.sqrt(3)
    hexagon_model = Model(((3/2, sqrt3/2), (0, sqrt3), (-3/2, sqrt3/2), (-3/2, -sqrt3/2), (0, -sqrt3), (3/2, -sqrt3/2)))
    hexahon_shape1 = Shape(hexagon_model, position=(WIDTH//2, HEIGHT//2+100), scaling_factor=30, rotation=0, color='')
    hexahon_shape2 = Shape(hexagon_model, position=(WIDTH//2+100, HEIGHT//2+100), scaling_factor=30, rotation=math.pi/2, color='')

    shapes = [triangle_shape1, triangle_shape2, hexahon_shape1, hexahon_shape2]

    root = tk.Tk()
    app = SymmetryVis(root)
    root.mainloop()
