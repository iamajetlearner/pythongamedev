import pgzrun
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
    camous.draw()
    mousat.draw()
def update():
    if keyboard.w:
        camous.y-=10
    elif keyboard.s:
        camous.y+=10
    elif keyboard.a:
        camous.x-=10
    elif keyboard.d:
        camous.x+=10
pgzrun.go()