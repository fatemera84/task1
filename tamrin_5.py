a=int(input("enter a size:"))
b=input("enter a color:")
import turtle
wn = turtle.Screen()
t=turtle.Turtle()
t.shape("turtle")
t.color(b)
for i in range (4):
    t.forward(a)
    t.right(90)
wn.mainloop()
