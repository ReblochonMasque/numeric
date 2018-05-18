import random
import tkinter as tk
from src.geometry import Point2D
from typing import NamedTuple
from copy import deepcopy

WIDTH, HEIGHT = 1200, 800
SCALE = 40
OFFX, OFFY = 10, -10
OFFSET = Point2D(OFFX, OFFY)


class Vector2D(Point2D):

    def __init__(self, x=0, y=0, anchor=Point2D(0, 0)):
        super().__init__(x, y)
        self.anchor = anchor

    def __str__(self):
        return f"{self.__class__.__name__}({', '.join(str(v) for v in self)}) anchored at: {self.anchor}"

    def get_coords(self):
        return self.anchor, self + self.anchor


def make_vector2D(point: Point2D, anchor=Point2D(0, 0)) -> Vector2D:
    x, y = point
    return Vector2D(x, y, anchor)


class Controls(tk.Frame):
    """
    controls shoot, angle, initial velocity
    """
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)

        self.x_value, self.y_value = tk.IntVar(0), tk.IntVar(0)

        self.shoot_btn = tk.Button(self, text='shoot', command=self.shoot_btn_pressed)
        self.shoot_btn.grid(row=0, column=5, rowspan=2, sticky=(tk.N, tk.S))

        self.decrease_x_btn = tk.Button(self, text='decrease x', command=self.decrease_x)
        self.decrease_x_btn.grid(row=0, column=0)
        self.increase_x_btn = tk.Button(self, text='increase x', command=self.increase_x)
        self.increase_x_btn.grid(row=0, column=1)
        self.x_label = tk.Label(self, textvariable=self.x_value)
        self.x_label.grid(row=0, column=2)

        self.decrease_y_btn = tk.Button(self, text='decrease y', command=self.decrease_y)
        self.decrease_y_btn.grid(row=1, column=0)
        self.increase_y_btn = tk.Button(self, text='increase y', command=self.increase_y)
        self.increase_y_btn.grid(row=1, column=1)
        self.y_label = tk.Label(self, textvariable=self.y_value)
        self.y_label.grid(row=1, column=2)

        self.pack()

    def shoot_btn_pressed(self):
        print('shoot button pressed')
        self.master.shoot()

    def increase_x(self):
        print('x increased')
        self.x_value.set(self.x_value.get() + 1)
        self.master.increase_x()

    def decrease_x(self):
        print('x decreased')
        self.x_value.set(self.x_value.get() - 1)
        self.master.decrease_x()

    def increase_y(self):
        print('y increased')
        self.y_value.set(self.y_value.get() + 1)
        self.master.increase_y()

    def decrease_y(self):
        print('y decreased')
        self.y_value.set(self.y_value.get() - 1)
        self.master.decrease_y()


class ShootingTheater(tk.Frame):
    """
    contains a canvas that draws grids, vectors, cannon, projectiles,
    targets, and trajectories
    """
    def __init__(self, master):
        self.master = master
        super().__init__(self.master, width=WIDTH, height=HEIGHT)
        self.canvas = tk.Canvas(self, bg='yellow', width=WIDTH, height=HEIGHT)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.pack(fill=tk.BOTH, expand=True)
        self.configure(width=WIDTH, height=HEIGHT)

        self.origin = Point2D(0, -HEIGHT)   # <-- shooting_theater origin relative to canvas top left corner

    def clear(self):
        self.canvas.delete("all")

    def draw_v_grid(self):
        for x in range(OFFX, WIDTH, SCALE):
            self.canvas.create_line(x, 0, x, HEIGHT, fill='grey80')

    def draw_h_grid(self):
        for y in range(HEIGHT+OFFY, 0, -SCALE):
            self.canvas.create_line(0, y, WIDTH, y, fill='grey80')

    def draw_target(self):
        pass

    def draw_projectile(self, pos: Point2D):
        x, y = self._convert_to_canvas_coordinates(pos)
        self.canvas.create_oval(x-3, y-3, x+3, y+3, fill='black')

    def draw_vectors(self):
        pass

    def draw_trajectory(self):
        pass

    def draw_vector(self, vec, color='blue', width=5):
        try:
            p0, p1 = vec.get_coords()
        except AttributeError:
            p0 = Point2D(0, 0)
            p1 = vec
        anchor = self._convert_to_canvas_coordinates(p0)
        v = self._convert_to_canvas_coordinates(p1)
        print(Point2D(0, 0), anchor)
        print(vec, v)
        self.canvas.create_line(*anchor, *v, fill=color, width=width, arrow=tk.LAST)

    def _convert_to_canvas_coordinates(self, point):
        x, y = point
        p = (SCALE * Point2D(x, -y)) - self.origin + OFFSET
        return p


class BallisticApp(tk.Frame):
    """Contains
    -> a canvas to display cannon, projectile, targets, and trajectory
    -> a control panel with command buttons
    """
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        self.control_panel = Controls(self)
        self.control_panel.pack()
        self.theater = ShootingTheater(self)
        self.theater.pack()
        self.pack()

        self.data = DataModel()
        self.trajectory = self.data.get_trajectory()

        self.draw()

    def shoot(self):
        self.data.shoot()
        self.draw()

    def increase_x(self):
        self.data.projectile.update_initial_velocity(Point2D(1, 0))
        self.draw()
        self.theater.draw_vector(self.data.projectile.velocity)

    def decrease_x(self):
        self.data.projectile.update_initial_velocity(Point2D(-1, 0))
        self.draw()
        self.theater.draw_vector(self.data.projectile.velocity)

    def increase_y(self):
        self.data.projectile.update_initial_velocity(Point2D(0, 1))
        self.draw()
        self.theater.draw_vector(self.data.projectile.velocity)

    def decrease_y(self):
        self.data.projectile.update_initial_velocity(Point2D(0, -1))
        self.draw()
        self.theater.draw_vector(self.data.projectile.velocity)

    def draw_unit_vectors(self):
        self.theater.draw_vector(self.data.e1)
        self.theater.draw_vector(self.data.e2)
        # v = make_vector2D(point=Point2D(3, 5), anchor=Point2D(1, 2))
        # self.theater.draw_vector(v)

    def draw(self):
        self.theater.clear()
        self.theater.draw_v_grid()
        self.theater.draw_h_grid()
        self.draw_unit_vectors()
        self.theater.draw_target()
        # self.theater.draw_projectile()
        self.theater.draw_vectors()
        for pos, vel, acc in self.trajectory:
            self.theater.draw_vector(pos, color='black', width=1)
            self.theater.draw_vector(vel, color='red', width=1)
            self.theater.draw_vector(acc, color='green', width=1)
            self.theater.draw_projectile(pos)

        self.theater.draw_trajectory()
        #################
        # self.draw_vector()


class DataModel:

    def __init__(self):
        self.e1 = Vector2D(x=1, y=0, anchor=Point2D(0, 0))
        self.e2 = Vector2D(x=0, y=1, anchor=Point2D(0, 0))

        self.projectile = Projectile()

    def shoot(self):
        self.projectile.calculate_trajectory()

    def get_trajectory(self):
        return self.projectile.trajectory


class Trajectory(NamedTuple):
    position: Point2D = Point2D(0, 0)
    velocity: Vector2D = Vector2D(0, 0, position)
    acceleration: Vector2D = Vector2D(0, -1, position)


class Projectile:

    def __init__(self):
        self.initial_position = Point2D(0, 0)
        self.position = deepcopy(self.initial_position)
        self.initial_velocity = Vector2D(0, 0, deepcopy(self.initial_position))
        self.velocity = deepcopy(self.initial_velocity)
        self.acceleration = Point2D(0, -1)
        self.t0 = 0
        self.dt = 1
        self.trajectory = [self.build_trajectory_point()]

    def update_initial_velocity(self, point: Point2D):
        self.initial_velocity += point
        self.velocity = deepcopy(self.initial_velocity)

    def update(self):
        self.position += self.velocity
        self.velocity += self.acceleration

    def calculate_trajectory(self):
        while self.position.y >= 0:
            self.update()
            self.trajectory.append(self.build_trajectory_point())

    def build_trajectory_point(self):
        vx, vy = self.velocity
        ax, ay = self.acceleration
        pos = deepcopy(self.position)
        return Trajectory(position=pos,
                          velocity=Vector2D(vx, vy, pos),
                          acceleration=Vector2D(ax, ay, pos))


if __name__ == '__main__':

    root = tk.Tk()
    app = BallisticApp(root)
    root.mainloop()
