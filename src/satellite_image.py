import turtle

if __name__ == '__main__':

    screen = turtle.Screen()
    path = '../resources/'
    gif_name = path + 'satellite.gif'
    screen.register_shape(gif_name)

    t = turtle.Turtle()
    t.shape(gif_name)

    screen.mainloop()
