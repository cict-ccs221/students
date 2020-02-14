import turtle
jl = turtle.Screen()
jl.bgcolor('lightblue')

shield = turtle.Turtle()
shield.color('white')
shield.speed(-1000)

for i in range(740):
    shield.forward(200)
    shield.right(30)
    shield.forward(20)
    shield.left(60)
    shield.forward(50)
    shield.right(30)
    
    shield.penup()
    shield.setposition(0, 0)
    shield.pendown()
    
    shield.right(.5)

club = turtle.Turtle()
club.color('red')
club.speed(-100)
for i in range(500):
    club.forward(i)
    club.left(200)
    
club = turtle.Turtle()
club.color('blue')
club.speed(100)
for i in range(310):
    club.forward(i)
    club.left(200)
    
club = turtle.Turtle()
club.color('white')
club.speed(100)
for i in range(150):
    club.forward(i)
    club.left(200)
    
Christian = turtle.Turtle()
Christian.speed(0)
Christian.color('lightblue')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Christian,115,5)
jl.exitonclick()

#improvised from Trinket & Michael0x2a code
