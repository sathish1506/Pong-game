import turtle
import threading
import time
import pygame.mixer

# Initialize pygame mixer
pygame.mixer.init()
score_A = 0
score_B = 0

#paddle collision sound
paddle_hit_sound = r"C:\Users\admin\OneDrive\Desktop\New folder\Python\.vscode\Project.py\PADDLE HIT SOUND.wav.mp3"
paddle_sound = pygame.mixer.Sound(paddle_hit_sound)
# victory sound
victory_music = r"C:\Users\admin\OneDrive\Desktop\New folder\Python\.vscode\Project.py\victory.wav.mp3"  
pygame.mixer.music.load(victory_music)

#defining for paddle sound
def play_paddle_hit_sound():
    paddle_sound.play()
#defining victory sound
def play_victory_music():
    pygame.mixer.music.play()
#display screen
win = turtle.Screen()
win.setup(800,600)
win.bgcolor("light blue")
win.title("Lee's pong game")
win.tracer(0)

#left_paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("brown")
left_paddle.shapesize(stretch_wid= 6 , stretch_len= 1)
left_paddle.penup()
left_paddle.goto(-385,0)
#right_paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("brown")
right_paddle.shapesize(stretch_wid= 6 , stretch_len= 1)
right_paddle.penup()
right_paddle.goto(385,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.dx = 1
ball.dy = 1

#score board display
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A :0  Player B : 0", align="center", font=("Futura", 18,"normal"))

# moving paddles

def left_paddle_up():
    left_paddle.sety(left_paddle.ycor()+20)
def left_paddle_down():
    left_paddle.sety(left_paddle.ycor()-20)

def right_paddle_up():
    right_paddle.sety(right_paddle.ycor()+20)
def right_paddle_down():
    right_paddle.sety(right_paddle.ycor()-20)

win.listen()
win.onkeypress(left_paddle_up,'w')
win.onkeypress(left_paddle_down,'s')

win.onkeypress(right_paddle_up,'Up')
win.onkeypress(right_paddle_down,'Down')

while True:
    win.update()
    #ball movement

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    # Ball - wall collision
 
    #top wall
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    #bottom wall
    if ball.ycor()<-284:
        ball.sety(-284)
        ball.dy *= -1
    #right wall
    if ball.xcor()>384:
        ball.setx(384)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write("Player A :{}  Player B : {}".format(score_A , score_B), align="center", font=("Futura", 18,"bold"))
     #left wall
    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write("Player A :{}  Player B : {}".format(score_A , score_B), align="center", font=("Futura", 18,"bold"))

    #collision with right paddle
    if ball.xcor()>370 and right_paddle.ycor()-50<ball.ycor() < right_paddle.ycor()+50 :
        ball.setx(360)
        ball.dx *= -1
        threading.Thread(target=play_paddle_hit_sound).start()
 
    #collision with left padle
    if ball.xcor()<-370 and left_paddle.ycor()-50<ball.ycor()< left_paddle.ycor()+50 :
        ball.setx(-360)
        ball.dx *= -1
        threading.Thread(target=play_paddle_hit_sound).start()
    if score_A >= 5 or score_B >= 5:
        winner = "Player A" if score_A >= 5 else "Player B"
        pen.clear()
        pen.goto(0,0)
        pen.write("{} wins!".format(winner), align="center", font=("arial", 18, "bold"))
        win.update()
        threading.Thread(target=play_victory_music).start()
        time.sleep(3)
        break
        
