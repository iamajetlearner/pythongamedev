import pgzrun
import random
score=0
game=True
WIDTH=500
HEIGHT=500
camous=Actor("cat")
mousat=Actor("mouse")
camous.y=100
camous.x=100
mousat.y=200
mousat.x=200
def draw():
    screen.blit("grassfield",(0,0))
    if game==True:
        camous.draw()
        mousat.draw()
        screen.draw.text(str(score),(50,50))
    else:
        screen.draw.text("game-over",(50,20))
def update():
    global score
    if keyboard.w:
        camous.y-=10
    elif keyboard.s:
        camous.y+=10
    elif keyboard.a:
        camous.x-=10
    elif keyboard.d:
        camous.x+=10
    if camous.colliderect(mousat):
        mousat.x =random.randint(100,400)
        mousat.y =random.randint(100,400)
        score+=1
def tomer():
    global game
    game=False
clock.schedule(tomer,10)
pgzrun.go()
