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
    app.icon = 'cube'
    app.iconCx = 250
    app.iconCy = app.groundY
    app.iconVelocity = 0
    app.gravity = 0.34
    app.inAir = False
    app.iconColorOuter = 'blue'
    app.iconColorInner = 'purple'
    app.crashed = False

    app.obstacleColor = gradient('dodgerBlue', 'navy', start = 'top')
    app.background = gradient('cyan', 'mediumBlue', start = 'top')
    app.groundColor = gradient('midnightBlue', 'blue', start = 'top')

    app.level1Obstacles = [Obstacles('spike', app.gridSize * 8, app.groundY),
        Obstacles('flat spike', app.gridSize * 24, app.groundY),
        Obstacles('spike', app.gridSize * 25, app.groundY),
        Obstacles('spike', app.gridSize * 44, app.groundY),
        Obstacles('spike', app.gridSize * 45, app.groundY),
        Obstacles('block', app.gridSize * 46, app.groundY),
        Obstacles('block', app.gridSize * 50, app.groundY, 2, 1),
        Obstacles('block', app.gridSize * 54, app.groundY, 3, 1),
        Obstacles('spike', app.gridSize * 78, app.groundY),
        Obstacles('spike', app.gridSize * 79, app.groundY),
        Obstacles('block', app.gridSize * 84, app.groundY, 1, 6),
        Obstacles('block', app.gridSize * 93, app.groundY, 1, 13),
        Obstacles('spike', app.gridSize * 99, app.groundY - app.gridSize),
        Obstacles('block', app.gridSize * 109, app.groundY-app.gridSize, 1, 13),
        Obstacles('spike', app.gridSize * 115, app.groundY -app.gridSize*2),
        Obstacles('block', app.gridSize * 125, app.groundY - app.gridSize * 2),
        Obstacles('block', app.gridSize * 129, app.groundY - app.gridSize * 3),
        Obstacles('block', app.gridSize * 133, app.groundY - app.gridSize * 4),
        Obstacles('block', app.gridSize * 137, app.groundY - app.gridSize * 5),
        Obstacles('block', app.gridSize * 141, app.groundY - app.gridSize * 2),
        Obstacles('block', app.gridSize * 145, app.groundY - app.gridSize * 3),
        Obstacles('block', app.gridSize * 149, app.groundY - app.gridSize * 4),
        Obstacles('block', app.gridSize * 153, app.groundY, 3, 23), 
        Obstacles('spike', app.gridSize * 158, app.groundY -app.gridSize*3),
        Obstacles('spike', app.gridSize * 159, app.groundY -app.gridSize*3),
        Obstacles('spike', app.gridSize * 160, app.groundY -app.gridSize*3),
        Obstacles('spike', app.gridSize * 161, app.groundY -app.gridSize*3),
        Obstacles('block', app.gridSize * 159, app.groundY-app.gridSize*(4+2/3), 
                  1/3, 1),
        Obstacles('block', app.gridSize * 160 ,app.groundY-app.gridSize*(4+2/3), 
                  1/3, 1),
        Obstacles('spike', app.gridSize * 167, app.groundY -app.gridSize*3),
        Obstacles('spike', app.gridSize * 168, app.groundY -app.gridSize*3),
        Obstacles('spike', app.gridSize * 169, app.groundY -app.gridSize*3),
        Obstacles('spike', app.gridSize * 170, app.groundY -app.gridSize*3),
        Obstacles('block', app.gridSize * 168, app.groundY-app.gridSize*(4+2/3), 
                  1/3, 1),
        Obstacles('block', app.gridSize * 169, app.groundY-app.gridSize*(4+2/3), 
                  1/3, 1), 
        Obstacles('block', app.gridSize * 176, app.groundY, 2, 10), 
        Obstacles('block', app.gridSize * 179, app.groundY-app.gridSize*(3+2/3), 
                  1/3, 1),
        Obstacles('spike', app.gridSize * 179, app.groundY- app.gridSize * 4),
        Obstacles('block', app.gridSize * 180, app.groundY-app.gridSize*(3+2/3), 
                  1/3, 1),
        Obstacles('spike', app.gridSize * 180, app.groundY- app.gridSize * 4),
        Obstacles('block', app.gridSize * 181, app.groundY-app.gridSize*(3+2/3), 
                  1/3, 1),
        Obstacles('spike', app.gridSize * 181, app.groundY- app.gridSize * 4),
        Obstacles('block', app.gridSize * 182, app.groundY-app.gridSize*(3+2/3), 
                  1/3, 1),
        Obstacles('spike', app.gridSize * 182, app.groundY- app.gridSize * 4),
        Obstacles('block', app.gridSize * 186, app.groundY, 3, 5),
        Obstacles('spike', app.gridSize * 190, app.groundY - app.gridSize * 3),
        Obstacles('block', app.gridSize * 191, app.groundY, 1, 10),
        Obstacles('spike', app.gridSize * 191, app.groundY - app.gridSize),
        Obstacles('block', app.gridSize * 203, app.groundY-app.gridSize* 2/3, 
                  1/3, 1),
        Obstacles('block', app.gridSize * 204, app.groundY-app.gridSize* 2/3, 
                  1/3, 1),
        Obstacles('block', app.gridSize * 205, app.groundY-app.gridSize* 2/3, 
                  1/3, 1),
        Obstacles('block', app.gridSize * 206, app.groundY-app.gridSize* 2/3, 
                  1/3, 1),
        Obstacles('block', app.gridSize * 207, app.groundY-app.gridSize* 2/3, 
                  1/3, 1),
        Obstacles('spike', app.gridSize * 207, app.groundY - app.gridSize),
        Obstacles('block', app.gridSize * 210, app.groundY-app.gridSize* 5/3, 
                  1/3, 1),
        Obstacles('block', app.gridSize * 211, app.groundY-app.gridSize* 5/3, 
                  1/3, 1),
        Obstacles('block', app.gridSize * 212, app.groundY-app.gridSize* 5/3, 
                  1/3, 1),
        Obstacles('block', app.gridSize * 213, app.groundY-app.gridSize* 5/3, 
                  1/3, 1),
        Obstacles('block', app.gridSize * 214, app.groundY-app.gridSize* 5/3, 
                  1/3, 1),
        Obstacles('spike', app.gridSize * 214, app.groundY - app.gridSize * 2),
        Obstacles('block', app.gridSize * 217, app.groundY, 1, 4),
        Obstacles('block', app.gridSize * 223, app.groundY, 2, 1),
        Obstacles('block', app.gridSize * 227, app.groundY, 3, 1),
        Obstacles('block', app.gridSize * 229, app.groundY, 2, 1), 
        Obstacles('block', app.gridSize * 233, app.groundY, 3, 1),
        Obstacles('block', app.gridSize * 236, app.groundY, 2, 1),
        Obstacles('block', app.gridSize * 240, app.groundY-app.gridSize*(2+2/3), 
                  1/3, 1),
        Obstacles('block', app.gridSize * 244, app.groundY-app.gridSize*(3+2/3), 
                  1/3, 1),
        Obstacles('block', app.gridSize * 248, app.groundY-app.gridSize*(4+2/3), 
                  1/3, 1),
        Obstacles('block', app.gridSize * 252, app.groundY-app.gridSize*(5+2/3), 
                  1/3, 1),
        Obstacles('block', app.gridSize * 256, app.groundY-app.gridSize*(6+2/3), 
                  1/3, 1),
        Obstacles('spike', app.gridSize * 256, app.groundY - app.gridSize * 7),
        Obstacles('block', app.gridSize * 255, app.groundY, 2, 20)
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
                fill = app.groundColor, border = 'white'))
        drawLevel1(app)
        drawIcon(app)
        if app.crashed:
            drawLabel('You Crashed!', app.width/2, 150, size = 40, fill = 'red',
                      font = 'monospace')
            drawLabel('''Press 'space' to retry''', app.width/2, 195, size = 25, 
                      fill = 'red', font = 'monospace')

def drawIcon(app):
    (drawRect(app.iconCx, app.iconCy, app.gridSize, app.gridSize, 
              fill = app.iconColorOuter, border = 'white' , borderWidth = 0.5,
              align = 'bottom-left')) 
    (drawRect(app.iconCx + app.gridSize/4, app.iconCy - app.gridSize/4, 
              app.gridSize/2, app.gridSize/2, 
              fill = app.iconColorInner, border = 'white' , borderWidth = 0.5,
              align = 'bottom-left')) 

def drawHomePage(app):
    (drawRect(0, app.groundY + 20, app.width, app.height - app.groundY, 
                fill = None, border = 'black'))
    drawLabel('Geometry Dash 112', app.width/2, app.height/4, size = 50, 
              font = 'monospace')
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
    drawLabel('Level 1', app.levelStartX - app.width/2, 175, size = 40, font = 'monospace')
    for i in range(len(app.level1Obstacles)):
        drawObstacle(app, app.level1Obstacles[i])

def drawObstacle(app, obstacle):
    vtxsCopy = copy.copy(obstacle.vtxs)
    for i in range(0, len(vtxsCopy), 2):
        vtxsCopy[i] += app.levelStartX
    drawPolygon(*vtxsCopy, fill = app.obstacleColor, border = 'white')

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
                        app.iconCy = (obstacle.bottomY - 
                                    (obstacle.height * app.gridSize))
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
        if ((app.width/2 - 50 <= mouseX <= app.width/2 + 50) and 
            (210 <= mouseY <= 290)):
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
        if app.crashed:
            app.crashed = False
                
def onStep(app):
    if app.currPage > 1:
        if not checkCollision(app, app.level1Obstacles):
            app.levelStartX -= 4.25
            if app.iconCy < app.groundY:
                app.inAir = True
            if app.inAir:
                app.iconCy += app.iconVelocity
                app.iconVelocity += app.gravity
                if app.iconCy > app.groundY:
                    app.iconCy = app.groundY
                    app.iconVelocity = 0
                    app.inAir = False
        else:
            app.iconColorOuter = 'red'
            app.iconColorInner = 'red'
            app.crashed = True

def main():
    runApp()

main()