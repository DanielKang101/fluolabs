add_library('minim')

beamX = []    # before setup()
beamY = []
superX = []
superY = []

shipX = []
shipY = []
speed = 1

gunX = 0
leftPressed = False
rightPressed = False
hitCount = 0
score = 0

def setup():
    global zapSound, crashSound, laserSound
    size(800, 800, P3D)
    minim = Minim(this)                             # setup()
    zapSound = minim.loadSample("zap.mp3")          # setup()
    laserSound = minim.loadSample("laser.wav")          # setup()
    
    for i in range(100):
        shipX.append(random(width) - width/2)
        shipY.append(random(height) - height/2)

    textSize(20)
    
def draw():
    global gunX, hitCount, shipX, shipY, score
    background(0)
    noFill()
    stroke(255)

    # display info
    text("score: " + str(score), 50, 50)
    text("hitCount: " + str(hitCount), 50, 80)

        
    translate(width/2, height/2)
    rotateX(radians(45))

    # show space ships
    for i in range(len(shipX)):
        stroke(random(256), random(256), random(256))
        rect(shipX[i], shipY[i], 50, 50)

    # update space ships
    for i in range(len(shipX)):
        shipY[i] = shipY[i] - speed
        if (shipY[i]  < -1000):
            shipY[i] = 800

    # laser gun
    stroke(255)
    y = height/2
    if (hitCount > 9):
        fill(255, 0, 0)
    else:
        fill(255)
    triangle(gunX - 20, y, gunX, y - 60, gunX + 20, y)

    # update gun location
    if (leftPressed):
        gunX -= 2
    if (rightPressed):
        gunX += 2
        
    # display beams :at the end of draw()
    strokeWeight(3)
    stroke(255, 255, 0)
    for i in range(len(beamX)):
        line(beamX[i], beamY[i], beamX[i], beamY[i] - 15)
        beamY[i] = beamY[i] - 10

    # remove invalid beams
    for i in range(len(beamX)-1, -1, -1):
        if (beamY[i] < -1200):
            del beamX[i]
            del beamY[i]
            
    # check beam hit
    loop_break = False
    for i in range(len(beamX)):
        for j in range(len(shipX)):
            if (shipX[j] < beamX[i]  and beamX[i] < shipX[j] + 50):
                if (shipY[j] + 50 > beamY[i] -15):
                    del shipX[j]
                    del shipY[j]
                    del beamX[i]
                    del beamY[i]
                    print("crash")
                    loop_break = True
                    #crashSound.trigger()
                    score += 10
                    hitCount += 1
  
                    break
        if loop_break: break
                
    # display super beams 
    strokeWeight(5)
    stroke(255, 0, 0)
    for i in range(len(superX)):
        line(superX[i], superY[i], superX[i], superY[i] - 40)
        superY[i] = superY[i] - 20

    # remove invalid beams
    for i in range(len(superX)-1, -1, -1):
        if (superY[i] < -1200):
            del superX[i]
            del superY[i]
            
    # check super beam hit
    loop_break = False
    #if len(beamX) > 0 and len(shipX) > 0:
    remShip = []
    for i in range(len(superX)):
        for j in range(len(shipX)):
            if (shipX[j] < superX[i]  and superX[i] < shipX[j] + 50):
                if (shipY[j] + 50 > superY[i] - 40):
                    score += 10
                    remShip.append(j)
                    #crashSound.trigger()  
    
    if (len(remShip) > 0):
        shipX = [x for i,x in enumerate(shipX) if i not in remShip]
        shipY = [x for i,x in enumerate(shipY) if i not in remShip]
                
def mouseClicked ():
    shipX.append(mouseX - width/2)
    shipY.append(mouseY - height/2)

def keyReleased():
    global leftPressed, rightPressed
    if (keyCode == LEFT):
        leftPressed = False
    elif (keyCode == RIGHT):
        rightPressed = False

def keyPressed():
    global leftPressed, rightPressed, hitCount, score
    if (keyCode == LEFT):
        leftPressed = True
    elif (keyCode == RIGHT):
        rightPressed = True
    elif (keyCode == 32):
        if hitCount > 9:
            superX.append(gunX)
            superY.append(height/2 - 50)
            hitCount = 0
            laserSound.trigger()
        else:
            beamX.append(gunX)
            beamY.append(height/2 - 50)
            score = score - 1
            zapSound.trigger() 
