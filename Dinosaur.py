score = 0 
time = 60
gameOver = False
x = 0 
y = 0
gliding = False
dSize = 50

def setup():
    size(480, 360)

def draw():
    global time, x, y, gameOver, gliding, glideCount, dSize
    background(0)
    textSize(20)
    text("score: " + str(score), 0 , 30)
    text("time: " + str(time), 0 , 50)
    if (frameCount % 120 == 0):
        time -= 2
        x = random(width)
        y = random(height)
        if (time < 30):
            dSize -= 5
            if (dSize < 10):
                dSize = 50
            
                            
    # check end of game
    if (time == 0):
        text("Game Over!", width/2- 50, height/2)
        gameOver = True
        noLoop()
    # animate gliding
    if (gliding):
        x += xGlide
        y += yGlide
        glideCount += 1 
        if (glideCount > 29):
            gliding = False
        
    # draw dinosaur
    ellipse(x, y, 30, 30)
    
def mouseClicked():
    global score, x, y, gliding, xGlide, yGlide, glideCount
    d = dist( x, y, mouseX, mouseY)
    if (d < dSize/2):
        score += 50
        gliding = True
        glideCount = 0
        destX = random(width)
        destY = random(height)
        xGlide = (destX - x)/30
        yGlide = (destY - y)/30
        if (time < 30):
            score += 50 - dSize
    else:
        score -= 10
        
