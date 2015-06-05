from graphics import *
from threading import Thread


mouseCoords = []

class Grid:
    mouseThread = None
    def __init__(self,start,end,rows,cols,color = 'black',win = None):
        self.start = Point(start[0],start[1])
        self.end = Point(end[0],end[1])
        self.cols = cols
        self.rows = rows
        self.color = color
        if(win is None):
            self.win = GraphWin('Grid',1000,1000)
            
        else:
            self.win = win
       
          
    #    if(not Grid.mouseThread):
     #         Grid.mouseThread = Thread(target = checkMouseClick,args = (self.win,))
    
        self.bottomLeft = Point(self.start.getX(),self.end.getY())
        self.topRight = Point(self.end.getX(),self.start.getY())
        
        
        #self.mouse = []

    def makeGrid(self):
            '''
            Makes a grid starting with the start point and ending with the end point in the window specified. The 
            grid consists of the rows and columns as specified in the arguments. The border color 
            of the grid is the color taken in the parameter. The default color is black.

            Arguments:
            start : Instance of Point object or a list with 2 elements
            end : Instance of Point object or a list with 2 elements
            rows : Positive Integer
            cols : Positive Integer

            DEFAULTS
            color : RGB value or a string of the name of the color.
            win : Instance of a window.
            '''

            topLine = Line(self.start,self.topRight)
            topLine.setOutline(self.color)
            topLine.draw(self.win)
            bottomLine = Line(self.bottomLeft,self.end)
            bottomLine.setOutline(self.color)
            bottomLine.draw(self.win)
            leftSide = Line(self.start,self.bottomLeft)
            leftSide.setOutline(self.color)
            leftSide.draw(self.win)
            rightSide = Line(self.topRight,self.end)
            rightSide.setOutline(self.color)
            rightSide.draw(self.win) 
   
  
            for i in range(0,self.cols):
                x = self.start.getX() * (1 - (float(i)/float(self.cols))) + self.topRight.getX() * (float(i) / float(self.cols))
                #print'x: ',x
                temp1 = Point(x,self.start.getY())
                x = self.bottomLeft.getX() * (1 - (float(i)/float(self.cols))) + self.end.getX() * (float(i) / float(self.cols))
                #print'x: ',x
                temp2 = Point(x,self.end.getY())
                tempLine = Line(temp1,temp2)
                tempLine.setOutline(self.color)
                tempLine.draw(self.win)
                #print(i)

            for i in range(0,self.rows):
                y = self.start.getY() * (1 - (float(i)/float(self.rows))) + self.bottomLeft.getY() * (float(i) / float(self.rows))
                #print'y: ',y
                temp1 = Point(self.start.getX(),y)
                y = self.topRight.getY() * (1 - (float(i)/float(self.rows))) + self.end.getY() * (float(i) / float(self.rows))
                #print'x: ',y
                temp2 = Point(self.end.getX(),y)
                tempLine = Line(temp1,temp2)
                tempLine.setOutline(self.color)
                tempLine.draw(self.win)
                #print(i)
            
           
       #     if(not Grid.mouseThread.isAlive()):
        #         Grid.mouseThread.start()
         #   return Grid.mouseThread
           

    def globalMap(self,row,col):
            
            '''
            Converts the Row-Column notation to the point-coordinate notation

            Arguments:
            row : Positive integer specifying the row number of the cell(row number starts with 0 and ends with m - 1 for mxn grid)
            col : Positive integer specifying the column number of the cell(column number starts with 0 and ends with n - 1 for mxn grid)
            
            RETURN VALUE:
            List of 2 Points that form the rectangular cell.
            '''
            '''
            if((row <= 0 or row >= maxRow) or (col <= 0 or col >= maxCol)):
                #throw error
            '''
            tempRow1 = self.start.getY() * (1 - (float(row)/float(self.rows))) + self.bottomLeft.getY() * (float(row) / float(self.rows))
            tempCol1 = self.start.getX() * (1 - (float(col)/float(self.cols))) + self.topRight.getX() * (float(col) / float(self.cols))
            #print tempCol1,tempRow1
            tempRow2 = self.start.getY() * (1 - (float(row + 1)/float(self.rows))) + self.bottomLeft.getY() * (float(row + 1) / float(self.rows))
            tempCol2 = self.start.getX() * (1 - (float(col + 1)/float(self.cols))) + self.topRight.getX() * (float(col + 1) / float(self.cols))
            #print tempCol2,tempRow2
            #self.markCell(Point(tempCol1,tempRow1),Point(tempCol2,tempRow2),'x')
            return [Point(tempCol1,tempRow1),Point(tempCol2,tempRow2)]

    def markCell(self,point1,point2,textstr,color = 'red'):
        p = Point((point1.getX() + point2.getX())/2,(point1.getY() + point2.getY())/2)
        #print p.getX(),p.getY()
        text = Text(p,textstr)
        text.setOutline(color)
        text.draw(self.win)
        
       
    def getMapPoint(self,row,col):
        tempRow1 = self.start.getY() * (1 - (float(row)/float(self.rows))) + self.bottomLeft.getY() * (float(row) / float(self.rows))
        tempCol1 = self.start.getX() * (1 - (float(col)/float(self.cols))) + self.topRight.getX() * (float(col) / float(self.cols))
        return Point(tempCol1,tempRow1)

    def fillCell(self,row,col,color = 'white'):
        templ = self.globalMap(row,col)
        tempShape = Rectangle(templ[0],templ[1])
        tempShape.setFill(color)
        tempShape.draw(self.win)

'''
--------------------------------TRASH-------------------------------------------------------------TRASH----------------------------------
    def checkMouseClick(self):
        
        takes a list l and updates it with the point coordinates of the cell selected with the mouse
        
        print 'Thread started'
        
        while(True):
            
            p = self.win.getMouse()
            print p.getX(),p.getY()
            if(p):
               rowColList = self.binSearch(p.getX(),p.getY())
               self.mouse = self.globalMap(rowColList[0],rowColList[1])
               print self.mouse
             
            self.win._onClick(self.win.checkMouse())

    def binSearch(self,point):
        begin = 0
        terminate = self.cols
        retList = []
        while(begin < terminate - 1):
            
            mid = (begin + terminate) / 2
            p = self.getMapPoint(0,mid)

            if(point.getX() == p.getX()):
                retList[0] = mid
                break
            elif(point.getX() < p.getX()):
                terminate = mid - 1
            else:
                begin = mid + 1

        retList[0] = begin

        begin = 0
        terminate = self.cols
        while(begin < terminate - 1):
            
            mid = (begin + terminate) / 2
            p = self.getMapPoint(mid,0)

            if(point.getY() == p.getY()):
                retList[1] = mid
                break
            elif(point.getY() < p.getY()):
                terminate = mid - 1
            else:
                begin = mid + 1
        retList[1] = begin
        self.globalMap(retList[0],retList[1])
        #return retList
         
def checkMouseClick(win):       
   
    takes a list l and updates it with the point coordinates of the cell selected with the mouse
        
    print 'Thread started'
        
    while(True):    
        p = win.getMouse()
        print 'Inside while'
        if(p):
            print 'Inside whiles if'
            print p.getX(),p.getY()
        
          mouseCoords = []
          mouseCoords.append(p)
          print mouseCoords
        '''
           
        #self.win._onClick(self.win.checkMouse())