print('Hello World')
from Grid import *
from random import randint
import time

win = GraphWin("Grid", 1000,1000)
win.setBackground('black')
obstacleList = {}
localMap = []
grid1 = Grid([50,300],[900,600],10,20,'red',win)
grid1.makeGrid()
grid2 = Grid([400,50],[600,200],3,3,'yellow',win)
grid2.makeGrid()
txt = Text(Point(500,250),'LOCAL MAP')
txt.setOutline('red')
txt.draw(win)
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
        
    
def setBot(row,col,color = 'blue'):
    templ = obstacleList.get(str(row)+':'+str(col))
    if(templ):
        return 0
    templ = grid1.globalMap(row,col)
    circ = Circle(Point((templ[0].getX() + templ[1].getX())/2,(templ[0].getY() + templ[1].getY())/2),5)
    if(color == 'white'):
        circ.setOutline('white')
    circ.setFill(color)
    circ.draw(win)
    #grid1.markCell(templ[0],templ[1],'O','yellow')
    return 1

def updateLocalMap(row,col):
    '''
    take bot position as input
    see the cells that it can see and color the appropriate edges of the local grid
    '''
    global localMap
    localMap = evaluatePosition(row,col)
    #print localMap
    updateChangestoLocalDisplay()

def evaluatePosition(row,col):
    lm = []
    for i in range(-1,2):
        for j in range(-1,2):
            if(i == 0 and j == 0):
                continue
            templ = obstacleList.get(str(row + i)+':'+str(col + j))
            if(templ):
                lm.append((i + 1,j + 1))
    if(row == 0):
        for i in range(0,3):
            lm.append((0,i))
    elif(row == grid1.rows - 1):
        for i in range(0,3):
            lm.append((2,i))
    if(col == 0):
        for i in range(0,3):
            lm.append((i,0))
    elif(col == grid1.cols - 1):
        for i in range(0,3):
            lm.append((i,2))
    return lm

def updateChangestoLocalDisplay():
    grid2.makeGrid()
    for element in localMap:
        #print 'Inside for'
        #print element
        templ = grid2.globalMap(element[0],element[1])
        tempShape = Rectangle(templ[0],templ[1])
        tempShape.setOutline('grey')
        tempShape.draw(win)

def moveBot():
    currentPosition = [0,0]
    lastPosition = [0,0]
    while(True):                                        #will be replaced by while(not (exitCondition()))
        templ = botTransition(currentPosition,lastPosition)
        #setBot(templ[0],templ[1])
        updateLocalMap(templ[0],templ[1])
        lastPosition = currentPosition
        currentPosition = templ
        updateGlobalMap(lastPosition,currentPosition)
        time.sleep(1)
        #if(not enter):
         #   continue

def botTransition(currPos,lastPos):
    templ = 1
    templocx = r1 = 0
    templocy = r2 = 0
    while(True):
        r1 = randint(-1,1)
        r2 = randint(-1,1)
        if(r1 == 0 and r2 == 0):
            continue
        templocx = currPos[0] + r1
        templocy = currPos[1] + r2
        
        if(templocx == lastPos[0] and templocy == lastPos[1]):
            continue

        if(checkConstraints(templocx,templocy)):
            break
    return [templocx,templocy]

def checkConstraints(x,y):
    #print x,y
    if((x < 0 or y < 0) or ((x > grid1.rows - 1) or (y > grid1.cols - 1))):
        return False
    elif(obstacleList.get(str(x)+':'+str(y))):
        return False
    else:
        return True

def updateGlobalMap(lp,cp):
    colorSpace(cp)
    setBot(lp[0],lp[1],'white')
    setBot(cp[0],cp[1])

def colorSpace(cp,color = 'white'):
    p = grid1.cellColorDict.get(str(cp[0])+':'+str(cp[1]))
    if(not p):
        grid1.fillCell(cp[0],cp[1])
        #print (grid1.cellColorDict.get(str(cp[0])+':'+str(cp[1])).config['fill'] == 'white')
    for i in range(-1,2):
        for j in range(-1,2):
            if(i == 0 and j == 0):
                continue
            x = cp[0] + i
            y = cp[1] + j
            if((x < 0 or y < 0) or ((x > grid1.rows - 1) or (y > grid1.cols - 1))):
                continue
            p = grid1.cellColorDict.get(str(x)+':'+str(y))
            if(not p):
                if(obstacleList.get(str(x)+':'+str(y))):
                    grid1.fillCell(x,y,'green')
                else:
                    grid1.fillCell(x,y)

                                        
setObstacles()
#grid1.fillCell(2,3)
#updateLocalMap(3,3)
grid1.fillCell(0,0)
setBot(0,0)
moveBot()
#print win.items

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