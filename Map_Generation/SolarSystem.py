#Solar system Animation

#important imports
import simpleguitk
import math


#Global parameters
WIDTH = 700
HEIGHT = 500

ball_pos = [WIDTH/2 , HEIGHT/2]


def update():
    ball_pos[0] += 1
    ball_pos[1] += 1
    
def draw(canvas):
    canvas.draw_circle([WIDTH/2 , HEIGHT/2], 100,1,"red")
    canvas.draw_circle(ball_pos, 20,1,"red", "red")
    update()

    
Frame = simpleguitk.create_frame("Solar System",WIDTH,HEIGHT)
Frame.set_draw_handler(draw)
Frame.start()
