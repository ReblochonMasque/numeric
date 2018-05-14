import tkinter as tk


WIDTH, HEIGHT = 500, 500


# class TransformWorldScreen:
#
#     """Internal class for 2-D coordinate transformations"""
#
#     def __init__(self, w, h, xlow, ylow, xhigh, yhigh):
#         # w, h are width and height of canvas
#         # (xlow,ylow) coordinates of lower-left [raw (0,h-1)]
#         # (xhigh,yhigh) coordinates of upper-right [raw (w-1,0)]
#         xspan = (xhigh-xlow)
#         yspan = (yhigh-ylow)
#         self.xbase = xlow
#         self.ybase = yhigh
#         self.xscale = xspan/float(w-1)
#         self.yscale = yspan/float(h-1)
#
#     def screen(self,x,y):
#         # Returns x,y in screen (actually canvas) coordinates
#         xs = (x-self.xbase) / self.xscale
#         ys = (self.ybase-y) / self.yscale
#         return int(xs+0.5),int(ys+0.5)
#
#     def world(self,xs,ys):
#         # Returns xs,ys in world coordinates
#         x = xs*self.xscale + self.xbase
#         y = self.ybase - ys*self.yscale
#         return x,y


class App(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.canvas = tk.Canvas(self.parent, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.pack()

        self.world = world
        self.world_scaling = 1
        self.canvas.bind('<1>', self.add_object)
        self.run()

    def add_object(self, event):
        x, y = event.x / self.world_scaling, event.y / self.world_scaling
        self.world.add_thing(TriangleShape, world_anchor=(x, y), scale=50)
        self.run()

    def run(self):
        for shape in self.world.things:
            self.canvas.create_polygon(shape.polygon)


class TriangleModel:

    def __init__(self):
        self.A, self.B, self.C = (-1, 0), (0, 1), (1, 0)
        self.polygon = [self.A, self.B, self.C]


class TriangleShape(TriangleModel):

    def __init__(self, world_anchor=(0, 0), scale_to_world=1):
        super().__init__()
        self.world_anchor = world_anchor
        self.scale_to_world = scale_to_world
        self.A = self.scale_to_world * self.A[0] + self.world_anchor[0], \
                 self.scale_to_world * self.A[1] + self.world_anchor[1]
        self.B = self.scale_to_world * self.B[0] + self.world_anchor[0], \
                 self.scale_to_world * self.B[1] + self.world_anchor[1]
        self.C = self.scale_to_world * self.C[0] + self.world_anchor[0], \
                 self.scale_to_world * self.C[1] + self.world_anchor[1]
        self.polygon = [self.A, self.B, self.C]


class World:

    def __init__(self):
        self.things = []

    def add_thing(self, thing, world_anchor=(0, 0), scale=1):
        self.things.append(thing(world_anchor=world_anchor, scale_to_world=scale))


if __name__ == '__main__':

    world = World()
    world.add_thing(TriangleShape, world_anchor=(-2, -3), scale=4)

    root = tk.Tk()
    app = App(root)
    root.mainloop()
