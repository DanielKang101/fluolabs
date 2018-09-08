
w = 600
h = 600
speed = 1

rectX = []
rectY = []

def setup():
    size(800, 800, P3D)

def draw():
    global y
    background(0)
    noFill()
    stroke(255)


    translate(width/2, height/2)
    rotateX(radians(45))
    
    # rect2
    for i in range(len(rectX)):
        rect(rectX[i]-width/2, rectY[i]-height/2, 50, 50)
        
    for i in range(len(rectX)):
        rectY[i] = rectY[i] - 1
    
    
def mouseClicked():
    rectX.append(mouseX)
    rectY.append(mouseY)
