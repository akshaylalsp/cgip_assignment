import turtle as t

# t.setworldcoordinates(0, t.window_height(), t.window_width(), 0)
t.hideturtle()
def bld(x:tuple,y:tuple):
    x1,y1=x
    x2,y2=y

    dx = x2-x1
    dy = y2-y1

    p = (2*dx)- dy

    for _ in range(0,max(dx,dy)):
        if p<0:
            x1,y1 = x1+1,y1
            p = p + (2*dy)
            t.goto(x1,y1)
        if p>0:
            x1,y1 = x1+1,y1+1
            p = p + (2*dy) - 2*dx
            t.goto(x1,y1)

bld((0,0),(100,636))

t.mainloop()
