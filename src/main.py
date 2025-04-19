from cmu_graphics import *

def onAppStart(app):
    app.width = 800
    app.height = 600
    app.sqSize = 200
    app.groundY = 400
    app.gridSize = 40

def redrawAll(app):
    drawRect(0, app.groundY, app.width, app.height - app.groundY, fill = None, border = 'black')
    drawSpike(app, 300, app.groundY)  
    drawBlock(app, 340, app.groundY)


def drawSpike(app, cx, cy):    
    (drawPolygon(cx, cy, cx + 20, cy - 40, cx + 40, cy, 
                fill = None, border='black'))
    
def drawBlock(app, cx, cy):
    (drawRect(cx, cy-app.gridSize, app.gridSize, 
              app.gridSize, fill = None, border = 'black'))

def main():
    runApp()

main()