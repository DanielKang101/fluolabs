
starx = []
stary = []
dias = []


d = 8

def setup():
    fullScreen()
    size(800,800) 
    background(0)

    for i in range(400):
        starx.append(random(width))
        stary.append(random(height))
        dias.append(random(2, 10))

def draw():
    background(0)
    global x,y
    fill(map(mouseX,0,width, 0, 256), 0, 0)
    
    for i in range(len(starx)):
        ellipse(starx[i],stary[i],dias[i],dias[i])
        starx[i] += 1
        stary[i] += 1
        
        if (starx[i] - d/2> width):
            starx[i] = random(width)
        if (stary[i] - d/2 > height):
            stary[i] = random(height)
        
