def setup():
    global motorboat, buoy
    #rectMode(CENTER)
    size(320,568)
    background(90,157 ,245)
    frameRate(10)
    motorboat = loadImage("motorboat.png")
    buoy = loadImage("buoy1.png")
    

#distance vars and stuff
meters = 0
metcount = 0


bx = 160

keyList = []

def draw():
    global meters, metcount, bx, motorboat, buoy
    #sun/sea
    fill(255,204,0)
    circle(160,80,100)
    fill(0,0,255)
    rect(0,150,320,448)
    
    #distance 
    if metcount >= 2:
        meters += 1
        metcount = 0
    elif metcount < 2:
        metcount += 1
    noStroke()
    fill(90,157 ,245)
    rect(200,0,150,40)
    fill(0,0,0)
    text("Meters = " + str(meters), 220,10)
    
    
    
    #boat
    image(motorboat, bx,500)
    
    
    
    if "d" in keyList:
        if bx < 313: 
            bx += 7
        else:
            bx = bx
    if "a" in keyList:
        if bx > 7:
            
    
            bx -= 7
        else:
            bx=bx
            
    drawBuoy(50,120)
            
            
def keyPressed():

    if key not in keyList:
        keyList.append(key)
    
    
def keyReleased():
    keyList.remove(key)
    
    
def drawBuoy(x,y):
    global buoy
    image(buoy,x,y)
