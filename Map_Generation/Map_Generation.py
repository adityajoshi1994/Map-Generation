print('Hello World')
from Grid import *

win = GraphWin("Grid", 1000,1000)
win.setBackground('black')
obstacleList = {}
localMap = []
grid1 = Grid([50,300],[900,600],10,20,'red',win)
grid1.makeGrid()
grid2 = Grid([400,50],[600,200],3,3,'yellow',win)
grid2.makeGrid()
l = grid2.globalMap(1,1)
grid2.markCell(l[0],l[1],'yolo')

def setObstacles():
    takeObstacles()

def takeObstacles():
    while(True):
        x,y = raw_input('Eneter the obstacle cell no: ').split()
        print x,y
        if(str(x) == 'done'):
            break;
        templ = grid1.globalMap(int(x),int(y))
        grid1.markCell(templ[0],templ[1],'x')
        obstacleList[x+':'+y] = templ
        
    
def setBot(row,col):
    templ = obstacleList.get(str(row)+':'+str(col))
    if(templ):
        return 0
    templ = grid1.globalMap(row,col)
    grid1.markCell(templ[0],templ[1],'O','yellow')
    return 1

def updateLocalMap(row,col):
    '''
    take bot position as input
    see the cells that it can see and color the appropriate edges of the local grid
    '''
    global localMap
    localMap = evaluatePosition(row,col)
    print localMap
    updateChangestoDisplay()

def evaluatePosition(row,col):
    lm = []
    for i in range(-1,2):
        for j in range(-1,2):
            if(i == 0 and j == 0):
                continue
            templ = obstacleList.get(str(row + i)+':'+str(col + j))
            if(templ):
                lm.append((i + 1,j + 1))
    return lm

def updateChangestoDisplay():
   
    for element in localMap:
        print 'Inside for'
        print element
        templ = grid2.globalMap(element[0],element[1])
        tempShape = Rectangle(templ[0],templ[1])
        tempShape.setOutline('grey')
        tempShape.draw(win)


    
setObstacles()
grid1.fillCell(2,3)
updateLocalMap(3,3)
#print setBot(0,0)


'''
-------------------------------TRASH-----------------------------------------------------------TRASH----------------------------
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

#while(True):
    #win.getMouse()

def showUp(element):
    pointl = []
    
    if(element[1] == 1):
        pointl.append(grid2.getMapPoint(element[0] + 1,element[1]))
        pointl.append(grid2.getMapPoint(element[0] + 1,element[1] + 1))
        
        tempLine = Line(pointl[0],pointl[1])
        tempLine.setOutline('grey')
        tempLine.draw(win)
    
    else:
        pointl.append(grid2.getMapPoint(element[0] + 1,element[1]))
        pointl.append(grid2.getMapPoint(element[0] + 1,element[1] + 1))
        pointl.append(grid2.getMapPoint(element[0],element[1]))
        tempLine = Line(pointl[0],pointl[1])
        tempLine.setOutline('grey')
        tempLine.draw(win)
        tempLine = Line(pointl[2],pointl[0])
        tempLine.setOutline('grey')
        tempLine.draw(win)

def showDown(element):
    pointl = []
    
    if(element[1] == 1):
        pointl.append(grid2.getMapPoint(element[0] + 1,element[1]))
        pointl.append(grid2.getMapPoint(element[0] + 1,element[1] + 1))
        
        tempLine = Line(pointl[0],pointl[1])
        tempLine.setOutline('grey')
        tempLine.draw(win)
    
    else:
        pointl.append(grid2.getMapPoint(element[0] ,element[1] + 1))
        pointl.append(grid2.getMapPoint(element[0] + 1,element[1] + 1))
        pointl.append(grid2.getMapPoint(element[0],element[1]))
        tempLine = Line(pointl[0],pointl[1])
        tempLine.setOutline('grey')
        tempLine.draw(win)
        tempLine = Line(pointl[2],pointl[0])
        tempLine.setOutline('grey')
        tempLine.draw(win)

def showSide(element):
    pointl = []
    
    if(element[1] == 0):
        pointl.append(grid2.getMapPoint(element[0],element[1] + 1))
        pointl.append(grid2.getMapPoint(element[0] + 1,element[1] + 1))
        
        tempLine = Line(pointl[0],pointl[1])
        tempLine.setOutline('grey')
        tempLine.draw(win)
    elif(element[1] == 2):
        pointl.append(grid2.getMapPoint(element[0],element[1]))
        pointl.append(grid2.getMapPoint(element[0] + 1,element[1]))
        
        tempLine = Line(pointl[0],pointl[1])
        tempLine.setOutline('grey')
        tempLine.draw(win)
    
    else:
        pointl.append(grid2.getMapPoint(element[0] + 1,element[1]))
        pointl.append(grid2.getMapPoint(element[0] + 1,element[1] + 1))
        pointl.append(grid2.getMapPoint(element[0],element[1]))
        tempLine = Line(pointl[0],pointl[1])
        tempLine.setOutline('grey')
        tempLine.draw(win)
        tempLine = Line(pointl[2],pointl[1])
        tempLine.setOutline('grey')
        tempLine.draw(win)

'''