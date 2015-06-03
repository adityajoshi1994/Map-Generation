print('Hello World')

#import simpleguitk 
#from graphics import *
from Grid import *
'''
from grid_display import *
def draw(canvas):
    canvas.draw_circle([320/2 , 240/2], 100,1,"red")
    canvas.draw_line((200,200),(300,300),1,'white')
    canvas.fillRect(320,240,100,120)
myFrame =  simpleguitk.create_frame('Hello Its me',320, 240)
myFrame.set_draw_handler(draw)
myFrame.start()
#win = GraphWin("Grid", 200, 300)
#win.setCoords(0,0,10,10)
win = GraphWin()
shape = Rectangle(Point(10,10),Point(20,20))
shape.setOutline('red')
shape.draw(win)
  '''
win = GraphWin("Grid", 1000,1000)
grid1 = Grid([50,300],[900,600],10,20,'red',win)
grid1.makeGrid()
grid2 = Grid([400,50],[600,200],3,3,'yellow',win)
grid2.makeGrid()
l = grid2.globalMap(0,0)
#grid2.markCell(l[0],l[1],'yolo')
grid2.mouseThread.join()
