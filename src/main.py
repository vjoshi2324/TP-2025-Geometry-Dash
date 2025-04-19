from cmu_graphics import *

def onAppStart(app):
    app.width = 800
    app.height = 600
    app.sqSize = 200
    app.groundY = 400
    app.gridSize = 40
    app.stepsPerSecond = 400
    app.levelStartX = app.width
    app.levelStartY = app.groundY

def redrawAll(app):
    drawRect(0, app.groundY, app.width, app.height - app.groundY, fill = None, border = 'black')
    drawLevel(app, app.levelStartX, app.levelStartY)

def drawLevel(app, leftX, bottomY):
    drawSpike(app, leftX, bottomY)

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
    app.levelStartX -= 1

def main():
    runApp()

main()