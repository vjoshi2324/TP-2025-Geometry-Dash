from cmu_graphics import *
import copy
from obstacles import Obstacles

def onAppStart(app):
    app.width = 800
    app.height = 600
    app.sqSize = 200
    app.groundY = 500
    app.gridSize = 50
    app.stepsPerSecond = 120
    app.levelStartX = app.width
    app.levelStartY = app.groundY
    app.currPage = 0
    app.icon = 'cube'
    app.iconCx = 250
    app.iconCy = app.groundY
    app.iconVelocity = 0
    app.gravity = 0.34
    app.inAir = False
    app.iconColorOuter = 'blue'
    app.iconColorInner = 'purple'
    app.crashed = False
    app.level1Obstacles = [Obstacles('spike', app.gridSize * 8, app.groundY),
        Obstacles('flat spike', app.gridSize * 29, app.groundY),
        Obstacles('spike', app.gridSize * 30, app.groundY),
        Obstacles('spike', app.gridSize * 50, app.groundY),
        Obstacles('spike', app.gridSize * 51, app.groundY),
        Obstacles('block', app.gridSize * 52, app.groundY),
        Obstacles('block', app.gridSize * 56, app.groundY, 2, 1),
        Obstacles('block', app.gridSize * 60, app.groundY, 3, 1),
        Obstacles('spike', app.gridSize * 81, app.groundY),
        Obstacles('spike', app.gridSize * 82, app.groundY),
        Obstacles('block', app.gridSize * 90, app.groundY, 1, 6),
        Obstacles('block', app.gridSize * 99, app.groundY, 1, 13),
        Obstacles('spike', app.gridSize * 105, app.groundY - app.gridSize),
        Obstacles('block', app.gridSize * 115, app.groundY-app.gridSize, 1, 13),
        Obstacles('spike', app.gridSize * 121, app.groundY -app.gridSize*2),
        Obstacles('block', app.gridSize * 131, app.groundY - app.gridSize * 2),
        Obstacles('block', app.gridSize * 135, app.groundY - app.gridSize * 3),
        Obstacles('block', app.gridSize * 139, app.groundY - app.gridSize * 4),
        Obstacles('block', app.gridSize * 143, app.groundY - app.gridSize * 5),
        Obstacles('block', app.gridSize * 147, app.groundY - app.gridSize * 2),
        Obstacles('block', app.gridSize * 151, app.groundY - app.gridSize * 3),
        Obstacles('block', app.gridSize * 155, app.groundY - app.gridSize * 4),
        Obstacles('block', app.gridSize * 159, app.groundY, 3, 23), 
        Obstacles('spike', app.gridSize * 164, app.groundY -app.gridSize*3),
        Obstacles('spike', app.gridSize * 165, app.groundY -app.gridSize*3),
        Obstacles('spike', app.gridSize * 166, app.groundY -app.gridSize*3),
        Obstacles('spike', app.gridSize * 167, app.groundY -app.gridSize*3),
        Obstacles('block', app.gridSize * 165, app.groundY - app.gridSize * (4+2/3), 
                  1/3, 1),
        Obstacles('block', app.gridSize * 166 , app.groundY - app.gridSize * (4+2/3), 
                  1/3, 1),
        Obstacles('spike', app.gridSize * 173, app.groundY -app.gridSize*3),
        Obstacles('spike', app.gridSize * 174, app.groundY -app.gridSize*3),
        Obstacles('spike', app.gridSize * 175, app.groundY -app.gridSize*3),
        Obstacles('spike', app.gridSize * 176, app.groundY -app.gridSize*3),
        Obstacles('block', app.gridSize * 174, app.groundY - app.gridSize * (4+2/3), 
                  1/3, 1),
        Obstacles('block', app.gridSize * 175 , app.groundY - app.gridSize * (4+2/3), 
                  1/3, 1), 
        Obstacles('block', app.gridSize * 182, app.groundY, 2, 10), 
        Obstacles('block', app.gridSize * 185, app.groundY-app.gridSize*(3+2/3), 
                  1/3, 1),
        Obstacles('spike', app.gridSize * 185, app.groundY- app.gridSize * 4),
        Obstacles('block', app.gridSize * 186, app.groundY-app.gridSize*(3+2/3), 
                  1/3, 1),
        Obstacles('spike', app.gridSize * 186, app.groundY- app.gridSize * 4),
        Obstacles('block', app.gridSize * 187, app.groundY-app.gridSize*(3+2/3), 
                  1/3, 1),
        Obstacles('spike', app.gridSize * 187, app.groundY- app.gridSize * 4),
        Obstacles('block', app.gridSize * 188, app.groundY-app.gridSize*(3+2/3), 
                  1/3, 1),
        Obstacles('spike', app.gridSize * 188, app.groundY- app.gridSize * 4),
        Obstacles('block', app.gridSize * 192, app.groundY, 3, 5),
        Obstacles('spike', app.gridSize * 196, app.groundY - app.gridSize * 3),
        Obstacles('block', app.gridSize * 197, app.groundY, 1, 10),
        Obstacles('spike', app.gridSize * 197, app.groundY - app.gridSize),
        Obstacles('block', app.gridSize * 209, app.groundY-app.gridSize* 2/3, 
                  1/3, 1),
        Obstacles('block', app.gridSize * 210, app.groundY-app.gridSize* 2/3, 
                  1/3, 1),
        Obstacles('block', app.gridSize * 211, app.groundY-app.gridSize* 2/3, 
                  1/3, 1),
        Obstacles('block', app.gridSize * 212, app.groundY-app.gridSize* 2/3, 
                  1/3, 1),
        Obstacles('block', app.gridSize * 213, app.groundY-app.gridSize* 2/3, 
                  1/3, 1),
        Obstacles('spike', app.gridSize * 213, app.groundY - app.gridSize),
        Obstacles('block', app.gridSize * 216, app.groundY-app.gridSize* 5/3, 
                  1/3, 1),
        Obstacles('block', app.gridSize * 217, app.groundY-app.gridSize* 5/3, 
                  1/3, 1),
        Obstacles('block', app.gridSize * 218, app.groundY-app.gridSize* 5/3, 
                  1/3, 1),
        Obstacles('block', app.gridSize * 219, app.groundY-app.gridSize* 5/3, 
                  1/3, 1),
        Obstacles('block', app.gridSize * 220, app.groundY-app.gridSize* 5/3, 
                  1/3, 1),
        Obstacles('spike', app.gridSize * 220, app.groundY - app.gridSize * 2)
        ]
    
def resetApp(app):
    app.levelStartX = app.width
    app.levelStartY = app.groundY
    app.iconCx = 250
    app.iconCy = app.groundY
    app.iconVelocity = 0
    app.gravity = 0.34
    app.inAir = False
    app.iconColorOuter = 'blue'
    app.iconColorInner = 'purple'
    
    
def redrawAll(app):
    if app.currPage == 0:
        drawHomePage(app)
    elif app.currPage == 1:
        drawLevelMenu(app)
    elif app.currPage == 2:
        (drawRect(0, app.groundY, app.width, app.height - app.groundY, 
                fill = None, border = 'black'))
        drawIcon(app)
        drawLevel1(app)

def drawIcon(app):
    (drawRect(app.iconCx, app.iconCy, app.gridSize, app.gridSize, 
              fill = app.iconColorOuter, align = 'bottom-left')) 
    (drawRect(app.iconCx + app.gridSize/4, app.iconCy - app.gridSize/4, 
              app.gridSize/2, app.gridSize/2, 
              fill = app.iconColorInner, align = 'bottom-left')) 

def drawHomePage(app):
    (drawRect(0, app.groundY + 20, app.width, app.height - app.groundY, 
                fill = None, border = 'black'))
    drawLabel('Geometry Dash 112', app.width/2, app.height/4, size = 50, font = 'monospace')
    (drawRect(app.width/2 - 50, 250, 100, 80, fill = None, border = 'black', 
             borderWidth = 5))
    drawLabel('PLAY', app.width/2, 290, size = 25, font = 'monospace')

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
        if (-1 * app.gridSize * 50) <= vtxsCopy[0] <= (app.width +app.gridSize):
            drawPolygon(*vtxsCopy, fill = None, border = 'black')

def checkCollision(app, L):
    for obstacle in L:
        vtxsCopy = copy.copy(obstacle.vtxs)
        for i in range(0, len(vtxsCopy), 2):
            vtxsCopy[i] += app.levelStartX
        if (app.iconCx - app.gridSize * obstacle.width < vtxsCopy[0] 
            < app.iconCx + app.gridSize):

            if obstacle.type == 'block':
                if (app.iconCy - app.gridSize < vtxsCopy[1] 
                    < app.iconCy + app.gridSize * obstacle.height):
                    if app.iconVelocity <= 0:
                        return True
                    else:
                        app.iconCy = obstacle.bottomY - (obstacle.height * app.gridSize)
                        app.iconVelocity = 0
                        app.inAir = False

            elif (obstacle.type == 'spike') or (obstacle.type == 'flat spike'):
                slope1 = (vtxsCopy[3] - vtxsCopy[1])/(vtxsCopy[2] - vtxsCopy[0])
                yInt1 = -1*(slope1 * vtxsCopy[0]) + vtxsCopy[1]
                check1 = slope1 * (app.iconCx + app.gridSize) + yInt1

                slope2 = (vtxsCopy[3] - vtxsCopy[5])/(vtxsCopy[2] - vtxsCopy[4])
                yInt2 = -1*(slope2 * vtxsCopy[4]) + vtxsCopy[5]
                check2 = slope2 * (app.iconCx) + yInt2
                
                if (app.iconCy - app.gridSize < vtxsCopy[1] 
                    < app.iconCy + app.gridSize):
                    if ((app.iconCx + app.gridSize) < vtxsCopy[2] and
                        app.iconCy < check1):
                        return False
                    elif (app.iconCx > vtxsCopy[2] and
                        app.iconCy < check2):
                        return False
                    return True

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
            if not (checkCollision(app, app.level1Obstacles) or app.inAir):
                app.inAir = True
                app.iconVelocity = -9
            if checkCollision(app, app.level1Obstacles):
                resetApp(app)

def onKeyHold(app, keys):
    if 'space' in keys:
        if not (checkCollision(app, app.level1Obstacles) or app.inAir):
                app.inAir = True
                app.iconVelocity = -9
            
                
def onStep(app):
    if app.currPage > 1:
        if not checkCollision(app, app.level1Obstacles):
            app.levelStartX -= 4.25
            if app.icon == 'cube':
                if app.iconCy < app.groundY:
                    app.inAir = True
                if app.inAir:
                    app.iconCy += app.iconVelocity
                    app.iconVelocity += app.gravity
                    if app.iconCy > app.groundY:
                        app.iconCy = app.groundY
                        app.iconVelocity = 0
                        app.inAir = False
            if app.icon == 'rocket':
                app.velocity = 6
        else:
            app.iconColorOuter = 'red'
            app.iconColorInner = 'red'
            app.crashed = True

def main():
    runApp()

main()