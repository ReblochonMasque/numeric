import tkinter as tk
from PIL import ImageTk
from PIL import Image


class SimpleApp:
    def __init__(self, master, image, **kwargs):
        self.master = master
        self.image = image
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()

        self.tkimage = ImageTk.PhotoImage(self.image)
        self.canvas_obj = self.canvas.create_image(250, 250, image=self.tkimage)
        self.angle = 0
        self.master.after(10, self.draw())

    def draw(self):
        self.canvas.delete(self.canvas_obj)
        self.tkimage = ImageTk.PhotoImage(self.image.rotate(self.angle))
        self.canvas_obj = self.canvas.create_image(250, 250, image=self.tkimage)
        self.master.after_idle(self.master.update)
        self.angle += 1
        self.angle %= 360
        self.master.after(10, self.draw)


def resize_image(image, width):
    w, h = image.size
    height = h * width//w
    return image.resize((width, height), Image.ANTIALIAS)


if __name__ == '__main__':

    root = tk.Tk()
    path = '../resources/'
    # img_name = path + 'satellite_2.png'
    img_name = path + 'USS_Enterprise.png'

    img = Image.open(img_name)
    img = resize_image(img, 200)
    print(img)
    app = SimpleApp(root, img)
    root.mainloop()
