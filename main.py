from turtle import Screen, Turtle

#screen details
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Sneky Snek')

#create snek initial body

x_cor = -20 #x coordinate
y_cor = 0 #y coordinate

for i in range(3):
    sneak_segment = Turtle()
    sneak_segment.penup()
    sneak_segment.color('white')
    sneak_segment.shape('square')
    sneak_segment.goto(x_cor,y_cor)
    x_cor +=20




screen.exitonclick()