import turtle as t

# t.setworldcoordinates(0, t.window_height(), t.window_width(), 0)
t.hideturtle()
def dda(p1:tuple,p2:tuple):
    x1,y1 = p1
    x2,y2 = p2

    dx = x2 - x1
    dy = y2 - y1
    steps = max(dx,dy)
    slope = dy/dx
    for _ in range(steps):
        if dy >= dx:
            x1,y1 = (x1+1/slope,y1+1)
            t.goto(x1,y1)
        else:
            x1,y1 = (x1+1,y1+1/slope)
            t.goto(x1,y1)
dda((0,0),(10,50))


t.mainloop()
