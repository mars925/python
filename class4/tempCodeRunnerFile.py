import turtle as t

t.shape("circle")
t.color("red")
t.speed(0)

for i in range(100):
    t.stamp()
    t.penup()
    t.right(20)
    t.forward(i * 2)