import tkinter as tk


WIDTH, HEIGHT = 1000, 1000


class AffineAxis:

    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2
        # assert e1 X e2 != 0      --> e1 and e2 from a basis


class AffineGrid(tk.Canvas):

    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        self.configure(width=WIDTH, height=HEIGHT)
        self.pack()

        self.ax_x = (0, 0, 1000, -60)
        self.x_lines = [list(self.ax_x)]
        self.dx = 20

        self.ax_y = (0, 0, 50, 1000)
        self.y_lines = [list(self.ax_y)]
        self.dy = 30

        self.make_grid_points()
        self.show_grid()

    def make_grid_points(self):
        for _ in range(0, HEIGHT, self.dy):
            new_y_line = self.y_lines[-1][:]
            new_y_line[0] += self.dy
            new_y_line[2] += self.dy
            self.y_lines.append(new_y_line)

        for _ in range(0, WIDTH, self.dx):
            new_x_line = self.x_lines[-1][:]
            new_x_line[1] += self.dx
            new_x_line[3] += self.dx
            self.x_lines.append(new_x_line)

    def show_grid(self):
        # self.create_line(self.ax_x)
        # self.create_line(self.ax_y)
        for line in self.x_lines:
            self.create_line(line, fill='gray60')
        for line in self.y_lines:
            self.create_line(line, fill='gray60')


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")

    grid = AffineGrid(root)

    root.mainloop()
