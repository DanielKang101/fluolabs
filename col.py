x = 50
xSpeed = 1 
col = 255

def setup():
    size(800, 800)

def draw():
    global x
    background(0)
    fill(col, 0,col)
    rect(x, height/2, 150, 75)
    x = x + xSpeed
    
    fill(255)
    text("x: " + str(x) + " xSpeed:" + str(xSpeed), width/2, 32)
    
    
def mouseClicked():
    global xSpeed, col
    
    
    col = random(100, 255)
    xSpeed = xSpeed * -1
    if (xSpeed > 0):
        xSpeed += 1
    else:
        xSpeed -= 1
        
