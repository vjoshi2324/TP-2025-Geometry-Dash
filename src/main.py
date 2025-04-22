from cmu_graphics import *
import copy
from obstacles import Obstacles

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
    app.iconCx = 250
    app.iconCy = app.groundY - app.gridSize/2
    app.iconVelocity = 0
    app.gravity = 0.335
    app.inAir = False
    app.crashed = False
    app.level1Obstacles = [Obstacles('spike', 0, app.groundY),
        Obstacles('flat spike', app.gridSize*20, app.groundY),
        Obstacles('spike', app.gridSize * 21, app.groundY),
        Obstacles('spike', app.gridSize * 41, app.groundY),
        Obstacles('spike', app.gridSize * 42, app.groundY),
        Obstacles('block', app.gridSize * 43, app.groundY),
        Obstacles('block', app.gridSize * 46, app.groundY, 2, 1),
        Obstacles('block', app.gridSize * 49, app.groundY, 3, 1),
        Obstacles('spike', app.gridSize * 69, app.groundY),
        Obstacles('spike', app.gridSize * 70, app.groundY),
        Obstacles('block', app.gridSize * 74, app.groundY, 1, 6),
        Obstacles('block', app.gridSize * 83, app.groundY, 1, 13),
        Obstacles('spike', app.gridSize * 89, app.groundY - app.gridSize),
        Obstacles('block', app.gridSize * 99, app.groundY - app.gridSize, 1, 13),
        Obstacles('spike', app.gridSize * 105, app.groundY -app.gridSize*2),
        ]

def redrawAll(app):
    if app.currPage == 0:
        drawHomePage(app)
    elif app.currPage == 1:
        drawLevelMenu(app)
    elif app.currPage == 2:
        (drawRect(0, app.groundY, app.width, app.height - app.groundY, 
                fill = None, border = 'black'))
        (drawRect(app.iconCx, app.iconCy, app.gridSize, app.gridSize, 
                  align = 'center'))
        drawLevel1(app)


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

def drawLevel1(app):
    for i in range(len(app.level1Obstacles)):
        drawObstacle(app, app.level1Obstacles[i])

def drawObstacle(app, obstacle):
        vtxsCopy = copy.copy(obstacle.vtxs)
        for i in range(0, len(vtxsCopy), 2):
            vtxsCopy[i] += app.levelStartX
        drawPolygon(*vtxsCopy, fill = None, border = 'black')

def checkCollision(app, L):
    for obstacle in L:
        if (app.iconCx - app.gridSize/2 < obstacle.leftX 
            < app.iconCx + app.gridSize/2):
            if obstacle.type == 'block':
                if not app.inAir:
                    if (app.iconCy + app.gridSize/2 
                        > obstacle.bottomY - app.gridSize):
                        app.crashed = True
                else:
                    if (app.iconCy + app.gridSize/2 
                        > obstacle.bottomY - app.gridSize):
                        app.iconCy = obstacle.bottomY - app.gridSize

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
            if not app.inAir:
                app.inAir = True
                app.iconVelocity = -9

def onKeyHold(app, keys):
    if 'space' in keys:
        if not app.inAir:
                app.inAir = True
                app.iconVelocity = -9
                
def onStep(app):
    if app.currPage > 1:
        app.levelStartX -= 4.25
        if app.inAir:
            app.iconCy += app.iconVelocity
            app.iconVelocity += app.gravity
            if app.iconCy > app.groundY - app.gridSize/2:
                app.iconCy = app.groundY - app.gridSize/2
                app.iconVelocity = 0
                app.inAir = False

def main():
    runApp()

main()