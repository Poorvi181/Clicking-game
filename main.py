import pgzrun,random
TITLE="Catch The Duck!"
WIDTH=500
HEIGHT=500
duck=Actor("duck")
message=""
def draw():
    screen.fill("light pink")
    duck.draw()
    screen.draw.text(message,center=(400,30),fontsize=30)
def update():
    pass

def on_mouse_down(pos):
    global message
    duck.x=pos[0]
    duck.y=pos[1]

pgzrun.go()