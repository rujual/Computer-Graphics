from graphics import *

win=GraphWin('CompGraphics',600,500)
#this line sets the screen width and initialises a window object that is used to call the later functions

#now we will make Point objects- vertices of the house as an array of Points

pt=[Point(0,0) for x in range(0,14)] #initialised a 14 length array using list-comprehension


pt[0]=Point(0,0)
pt[1]=Point(115,449)
pt[2]=Point(115,237)

#similarly, check the pixel coordinate in Paint, and make a point for all vertices

pt[3]=Point(259,237)
pt[4]=Point(259,449)
pt[5]=Point(515,237)
pt[6]=Point(515,449)
pt[7]=Point(203,143)  #tip of the triangle
pt[8]=Point(197,79)
pt[9]=Point(61,259)
pt[10]=Point(101,245)
pt[11]=Point(275,255)
pt[12]=Point(547,245)
pt[13]=Point(459,83)

#using for loop, give win.draw

for x in pt:
    x.draw(win)

#now we can start drawing the borders and rectagular shapes such as walls, doors and windows

#in graphics, you only need to give the opposite
#points as paramters to draw a rectangle


r1=Rectangle(pt[1],pt[3])
r1.draw(win)
r1.setFill('blue')#this will fill the rectangle with blue

#lets see how this looks
#similarly, we can make the other wall of the house, and also
#the door and windows using the rectangle function

r2=Rectangle(pt[3],pt[6])
r2.draw(win)
r2.setFill('blue')

w1=Rectangle(Point(289,278),Point(368,353))
w1.draw(win)
w1.setFill('white')

w2=Rectangle(Point(407,270),Point(487,346))
w2.draw(win)
w2.setFill('white')

door=Rectangle(Point(152,273),Point(217,449))
door.draw(win)
door.setFill('maroon')

#let us have a nice golden doorknob also, which we can draw using the Circle function

#Circle function takes two parameters- centre point and radius in pixels


doorknob=Circle(Point(165,340),5)
doorknob.draw(win)
doorknob.setFill('yellow')

#finally, let us proceed to draw the roof of the house,
#the roof has an irregular shape
#it can be constructed using the Polygon function
#Polygon takes a list of all vertices in sequence as a single parameter


roof=Polygon([pt[8],pt[7],pt[11],pt[12],pt[13]])
roof.draw(win)
roof.setFill('red')

roof2=Polygon([pt[8],pt[7],pt[10],pt[9]])
roof2.draw(win)
roof2.setFill('red')

triangle=Polygon([pt[3],pt[2],pt[7]])
triangle.draw(win)#oops
triangle.setFill('maroon')
triangle.setOutline('maroon')
triangle.setWidth(8)

#now to have a nice sun and grass in the picture

sun=Circle(Point(75,61),30)
sun.draw(win)
sun.setFill('yellow')

grass=Rectangle(Point(0,400),Point(600,500))
grass.draw(win)
grass.setFill('light green')

win.setBackground('light yellow')
win.getMouse() #this will close the viewing window on-Click
win.close()



