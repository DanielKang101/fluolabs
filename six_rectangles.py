def setup():
    size(800, 800)
    fullScreen()

def draw():
    background(0)
    w = 100
    h = 50
    
    w = mouseX
    w = map(w, 0, width, 0, 200)
    h = mouseY
    h = map(h, 0, height, 0 , 200)

    # blue 1, 2
    fill(0, 0, random(255))
    rect(0, 0, w, h)
    rect(w*2, h*2, w, h)
    
    # green 2, 5
    fill(0, random(255), 0)
    rect(w, h, w, h)
    rect(w*4, h*4, w, h)
    
    # red 4, 6
    fill(random(255), 0, 0)
    rect(w*3, h*3, w, h)
    rect(w*5, h*5, w, h) 
    
    print(mouseX, mouseY)
