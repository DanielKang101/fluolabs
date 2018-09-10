shipX = []
shipY = []
gunX = 0
w = 600
h = 600
speed = 1
leftPressed = False
rightPressed = False


def setup(): 
    size(800, 800, P3D)
    
def draw():
    global gunX
    background(0)
    
    noFill()
    stroke(255)
    
    text("ships: " + str(len(shipX)), 0, 50)

    translate(width/2, height/2)
    rotateX(PI/4)
    
    # space ships
    for i in range(len(shipX)):
        stroke(random(256), random(256), random(256))
        rect(shipX[i] - width/2, shipY[i] - height/2 , 50, 50)
    # update space ships
    for i in range(len(shipY)):
        shipY[i] = shipY[i] - speed
    
    # laser gun
    stroke(255)
    y = height/2
    triangle(gunX - 20, y, gunX, y - 60, gunX + 20, y)
    
    # update gun location
    if (leftPressed):
        gunX -=2
    if (rightPressed):
        gunX += 2

    
def mouseClicked():
    shipX.append(mouseX)
    shipY.append(mouseY)
    
def keyReleased():
    global leftPressed, rightPressed
    if (keyCode == LEFT):
        leftPressed = False
    elif (keyCode == RIGHT):
        rightPressed = False
 
def keyPressed():
    global leftPressed, rightPressed
    if (keyCode == LEFT):
        leftPressed = True
    elif (keyCode == RIGHT):
        rightPressed = True
        
    

