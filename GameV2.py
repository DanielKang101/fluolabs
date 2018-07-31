x = 50
xSpeed = 1
col = 255
strike = 0
rectWidth = 500

def setup():
    size(800,800)
    fullScreen()
    
def draw():
    global x, strike
    background(0)
    fill(col,0,0)
    rect(x, height/2, rectWidth, 75)
    x += xSpeed
    
    fill(255)
    text("xSpeed: " + str(xSpeed), width/2, 32)
    text("xSpeed: " + str(x), width/2, 48)
    text("strike: " + str(strike), width/2, 64)
    #check game over
    if (strike == 3):
        textSize(64)
        text("Game Over, GG", width/2 -rectWidth, height/2)
        noLoop()
    
    #check boundary
    if (x > width):
        x = rectWidth * -1
        strike += 1
    if (x + rectWidth < 0):
        x = width
        strike += 1
    
    
def mouseClicked():
    global xSpeed, col, rectWidth
        
        
    #check boundary
    if ((mouseX > x) and (mouseX < x + rectWidth)):
        if ((mouseY > height/2) and (mouseY< height/2 + 75)):
            xSpeed *= -1
            col = random(100, 256)
            
            if (rectWidth > 100):
                rectWidth -= 20
            
            
        if (xSpeed > 0):
            xSpeed += 1
        else:
            xSpeed -= 1
