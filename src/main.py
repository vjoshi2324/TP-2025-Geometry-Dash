from cmu_graphics import *

def onAppStart(app):
    app.width = 800
    app.height = 600
    app.sqSize = 200
    app.groundY = 400
    app.gridSize = 50
    app.stepsPerSecond = 60
    app.levelStartX = app.width
    app.levelStartY = app.groundY

def redrawAll(app):
    (drawRect(0, app.groundY, app.width, app.height - app.groundY, 
              fill = None, border = 'black'))
    drawLevel1(app, app.levelStartX, app.levelStartY)

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
    
def onStep(app):
    app.levelStartX -= 10

def main():
    runApp()

main()