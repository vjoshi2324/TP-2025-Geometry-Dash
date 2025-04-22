from cmu_graphics import *
from jumpPhysics import jumpPhysics

def onAppStart(app):
    app.width = 800
    app.height = 600
    app.sqSize = 200
    app.groundY = 400
    app.gridSize = 50
    app.stepsPerSecond = 120
    app.levelStartX = app.width
    app.levelStartY = app.groundY
    app.currPage = 0
    #app.icon = jumpPhysics(20, -4, app.groundY - app.gridSize/2, app.groundY - app.gridSize/2)
    app.cx = 250
    app.cy = app.groundY - app.gridSize/2
    app.iconVelocity = 0
    app.gravity = 0.4
    app.isJumping = False

def redrawAll(app):
    if app.currPage == 0:
        drawHomePage(app)
    elif app.currPage == 1:
        drawLevelMenu(app)
    elif app.currPage == 2:
        (drawRect(0, app.groundY, app.width, app.height - app.groundY, 
                fill = None, border = 'black'))
        drawRect(app.cx, app.cy, app.gridSize, app.gridSize, align = 'center')
        drawLevel1(app, app.levelStartX, app.levelStartY)

def drawHomePage(app):
    (drawRect(0, app.groundY + 20, app.width, app.height - app.groundY, 
                fill = None, border = 'black'))
    drawLabel('Geometry Dash 112', app.width/2, app.height/4, size = 50)
    (drawRect(app.width/2 - 50, 250, 100, 80, fill = None, border = 'black', 
             borderWidth = 5))
    (drawPolygon(app.width/2 - 20, 270, app.width/2 - 20, 310, app.width/2 + 30, 
                290, fill = None, border = 'black', borderWidth = 5))

def drawLevelMenu(app):
    drawLabel('Select a level!', app.width/2, app.height/5, size = 30)
    
    drawRect(100, 200, 225, 125, fill = None, border = 'black')
    drawLabel('Level 1', 100 + 225/2, 200+ 125/2, size = 20)
    
    drawRect(100, 400, 225, 125, fill = None, border = 'black')
    drawLabel('Level 2', 100 + 225/2, 400+ 125/2, size = 20)
    
    drawRect(475, 200, 225, 125, fill = None, border = 'black')
    drawLabel('Level 3', 475 + 225/2, 200+ 125/2, size = 20)
    
    drawRect(475, 400, 225, 125, fill = None, border = 'black')
    drawLabel('Demo Mode', 475 + 225/2, 400+ 125/2, size = 20)

def drawLevel1(app, leftX, bottomY):
    drawSpike(app, leftX, bottomY)
    drawFlatSpike(app, leftX + app.gridSize * 20, bottomY)
    drawSpike(app, leftX + app.gridSize * 21, bottomY)
    drawSpike(app, leftX + app.gridSize * 41, bottomY)
    drawSpike(app, leftX + app.gridSize * 42, bottomY)
    drawBlock(app, leftX + app.gridSize * 43, bottomY)
    drawStack(app, leftX + app.gridSize * 46, bottomY, 2)
    drawStack(app, leftX + app.gridSize * 49, bottomY, 3)
    drawSpike(app, leftX + app.gridSize * 69, bottomY)
    drawSpike(app, leftX + app.gridSize * 70, bottomY)
    drawBlockRow(app, leftX + app.gridSize * 74, bottomY, 6)
    drawBlockRow(app, leftX + app.gridSize * 83, bottomY, 13)
    drawSpike(app, leftX + app.gridSize * 89, bottomY - app.gridSize)
    drawBlockRow(app, leftX + app.gridSize * 99, bottomY - app.gridSize, 13)
    drawSpike(app, leftX + app.gridSize * 105, bottomY - app.gridSize * 2)

def drawStack(app, leftX, bottomY, height):
    for i in range(height):
        drawBlock(app, leftX, bottomY - app.gridSize * i)

def drawBlockRow(app, leftX, bottomY, width):
    for i in range(width):
        drawBlock(app, leftX + app.gridSize * i, bottomY)

def drawSpike(app, leftX, bottomY):    
    (drawPolygon(leftX, bottomY, leftX + app.gridSize/2, bottomY - app.gridSize,
                 leftX + app.gridSize, bottomY, fill = None, border='black'))

def drawFlatSpike(app, leftX, bottomY):    
    (drawPolygon(leftX, bottomY, leftX + app.gridSize/2, 
                 bottomY - app.gridSize/3, leftX + app.gridSize, bottomY, 
                 fill = None, border='black'))
    
def drawBlock(app, leftX, bottomY):
    (drawRect(leftX, bottomY-app.gridSize, app.gridSize, 
              app.gridSize, fill = None, border = 'black'))

def onMousePress(app, mouseX, mouseY):
    if app.currPage == 0:
        if (app.width/2 - 50 <= mouseX <= app.width/2 + 50) and (210 <= mouseY <= 290):
            app.currPage = 1
    elif app.currPage == 1:
        if (100 <= mouseX <= 325) and (200 <= mouseY <= 325):
            app.currPage = 2

def onKeyPress(app, key):
    if app.currPage > 1:
        if key == 'space':
            if not app.isJumping:
                app.isJumping = True
                app.iconVelocity = -10
                
def onStep(app):
    if app.currPage > 1:
        app.levelStartX -= 3.25
    if app.isJumping:
        app.cy += app.iconVelocity
        app.iconVelocity += app.gravity
        if app.cy > app.groundY - app.gridSize/2:
            app.cy = app.groundY - app.gridSize/2
            app.iconVelocity = 0
            app.isJumping = False

        


def main():
    runApp()

main()