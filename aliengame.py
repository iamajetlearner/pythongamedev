import pgzrun
import random
game=True
WIDTH=500
HEIGHT=500
alie = Actor("alien")
alie.x=100
alie.y=100
score=0
def draw():
    screen.fill("blue")
    if game==True: 
        alie.draw()
        screen.draw.text(str(score),(50,50))
    else:
        screen.draw.text("game-over",(50,20))
        screen.draw.text(str(score),(50,50))
def on_mouse_down(pos):
    global score
    if alie.collidepoint(pos): 
        alie.x =random.randint(100,500)
        alie.y =random.randint(100,500)
        score+=1
def timer():
    global game
    game=False
clock.schedule(timer,10)
pgzrun.go()