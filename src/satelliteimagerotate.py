import tkinter as tk
from PIL import ImageTk
from PIL import Image


class SimpleApp:
    def __init__(self, master, image, **kwargs):
        self.master = master
        self.image = image
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()

        self.update = self.draw().__next__
        master.after(100, self.update)

    def draw(self):
        angle = 0
        while True:
            tkimage = ImageTk.PhotoImage(self.image.rotate(angle))
            canvas_obj = self.canvas.create_image(
                250, 250, image=tkimage)
            self.master.after_idle(self.update)
            yield
            self.canvas.delete(canvas_obj)
            angle += 1
            angle %= 360


def resize_image(image, width):
    w, h = image.size
    height = h * width//w
    return image.resize((width, height), Image.ANTIALIAS)


if __name__ == '__main__':

    root = tk.Tk()
    path = '/Volumes/Extended/Docs/projects/threedee/threedee/resources/'
    # img_name = path + 'satellite_2.png'
    img_name = path + 'USS_Enterprise.png'

    img = Image.open(img_name)
    img = resize_image(img, 200)
    print(img)
    app = SimpleApp(root, img)
    root.mainloop()
