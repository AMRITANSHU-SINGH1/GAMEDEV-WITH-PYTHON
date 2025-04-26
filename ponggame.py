import turtle as tur
import winsound

wn=tur.Screen()
wn.title("pong by amritanshu")
wn.bgcolor("black")
wn.setup(width=800 , height=600)
wn.tracer(1) # stops the window from updating
# score
score_a=0
score_b=0

#paddle a

paddle_a=tur.Turtle() # Turtle is the class name
paddle_a.speed(0)  #by default the size is 20X 20 pixel
paddle_a.shape('square')
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()  
paddle_a.goto(-350,0)
#paddle b

paddle_b=tur.Turtle() # Turtle is the class name
paddle_b.speed(0)  #by default the size is 20X 20 pixel
paddle_b.shape('square')
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()  
paddle_b.goto(350,0)

#ball 


ball=tur.Turtle() # Turtle is the class name
ball.speed(0)  #by default the size is 20X 20 pixel
ball.shape('square')
ball.color("white")
ball.penup()  
ball.goto(0,0)
ball.dx=4 # this is the speed

ball.dy=4 #evry time our ball moves by two pixels


#pen
pen=tur.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B:0",align="center",font=("Times New Roman",24,"normal"))


# functions 

# we need paddle a to up and down same with b

def paddle_a_up():
     y=paddle_a.ycor()
     y+=20
     paddle_a.sety(y)

def paddle_a_down():
     y=paddle_a.ycor()
     y-=20
     paddle_a.sety(y)

def paddle_b_up():
     y=paddle_b.ycor()
     y+=20
     paddle_b.sety(y)

def paddle_b_down():
     y=paddle_b.ycor()
     y-=20
     paddle_b.sety(y)
# key board binding

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
# main game loop
while True:
     wn.update()
     # move the ball
     ball.setx(ball.xcor()+ball.dx)
     ball.sety(ball.ycor()+ball.dy)

     # border checking 
     # as per earlier we have defined the size of the widow
     if ball.ycor()>290:
          ball.sety(290)
          ball.dy *=-1
          winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
     
     if ball.ycor()<-290:
          ball.sety(-290)
          ball.dy *=-1
          winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
     
     if ball.xcor()>390:
          ball.goto(0,0)
          ball.dx *=-1
          score_a+=2
          pen.clear()
          pen.write(f"Player A:{score_a}  Player B:{score_b}",align="center",font=("Courier",24,"normal"))
     
     if ball.xcor()<-390:
          ball.goto(0,0)
          ball.dx *=-1
          score_b+=1
          pen.clear()
          pen.write(f"Player A:{score_a}  Player B:{score_b}",align="center",font=("Times New Roman",24,"normal"))
     # paddle and ball colliosn

     if ((ball.xcor()>340  and ball.xcor()<350) and 
          (ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50)): 
          ball.setx(340)
          ball.dx *= -1
          winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
     
     if ((ball.xcor()<-340  and ball.xcor()>-350) and 
          (ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50)): 
          ball.setx(-340)
          ball.dx *= -1
          winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
