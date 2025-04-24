from cmu_graphics import *
import copy
import os, pathlib
from obstacles import Obstacles

def onAppStart(app):
    ## Music from original Geometry Dash game, downloaded from Internet Archive
    app.level1Music = loadSound('/Users/vishakhajoshi2324/Documents/15-112/level1Music0.mp3')
    app.menuMusic = loadSound('/Users/vishakhajoshi2324/Documents/15-112/menuMusic.mp3')
    app.menuMusic.play(loop = True)

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
    app.iconColorOuter = gradient('dimGray', 'black', start ='center')
    app.iconColorInner = gradient('white', 'silver', start ='center')
    app.crashed = False
    app.steps = 0
    app.iconNum = 3
    app.iconColorList = ['Red', 'Orange', 'Yellow', 'Light Green', 'Green',
                         'Light Blue', 'Blue', 'Light Purple', 'Purple', 
                         'Light Pink', 'Pink']
    app.iconColorPairs = [('red', 'darkRed'),
                          ('orange', 'darkOrange'),
                          ('yellow', 'gold'),
                          ('paleGreen', 'mediumSpringGreen'),
                          ('limeGreen', 'green'),
                          ('lightSkyBlue', 'deepSkyBlue'),
                          ('dodgerBlue', 'blue'),
                          ('mediumOrchid', 'darkOrchid'),
                          ('blueViolet', 'indigo'),
                          ('plum', 'orchid'),
                          ('hotPink', 'deepPink')
                          ]


    app.obstacleColor = gradient('dodgerBlue', 'navy', start = 'top')
    app.background = gradient('darkMagenta', 'indigo', start = 'center')
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
        Obstacles('block', app.gridSize * 255, app.groundY, 2, 20), 
        Obstacles('block', app.gridSize * 265, app.groundY - app.gridSize * 2),
        Obstacles('spike', app.gridSize * 265, app.groundY - app.gridSize * 3),
        Obstacles('spike', app.gridSize * 275, app.groundY), 
        Obstacles('spike', app.gridSize * 280, app.groundY),
        Obstacles('spike', app.gridSize * 281, app.groundY),
        Obstacles('block', app.gridSize * 282, app.groundY, 1, 2),
        Obstacles('block', app.gridSize * 286, app.groundY-app.gridSize*(2/3), 
                  1/3, 2),
        Obstacles('block', app.gridSize * 291, app.groundY-app.gridSize*(1+2/3), 
                  1/3, 2),
        Obstacles('block', app.gridSize * 294, app.groundY, 1, 2),
        Obstacles('block', app.gridSize * 298, app.groundY-app.gridSize*(1+2/3), 
                  1/3, 2),
        Obstacles('spike', app.gridSize * 300, app.groundY),
        Obstacles('spike', app.gridSize * 301, app.groundY),

        
        Obstacles('spike', app.gridSize * 308, app.groundY),
        Obstacles('block', app.gridSize * 308, app.groundY - app.gridSize*4),
        Obstacles('block', app.gridSize * 308, app.groundY - app.gridSize*5),
        
        Obstacles('spike', app.gridSize * 309, app.groundY),
        Obstacles('block', app.gridSize * 309, app.groundY - app.gridSize*4),
        Obstacles('block', app.gridSize * 309, app.groundY - app.gridSize*5),
        
        Obstacles('spike', app.gridSize * 315, app.groundY),
        Obstacles('block', app.gridSize * 315, app.groundY - app.gridSize*4),
        Obstacles('block', app.gridSize * 315, app.groundY - app.gridSize*5),
        Obstacles('spike', app.gridSize * 316, app.groundY),
        Obstacles('block', app.gridSize * 316, app.groundY - app.gridSize*4),
        Obstacles('block', app.gridSize * 316, app.groundY - app.gridSize*5),
        Obstacles('spike', app.gridSize * 317, app.groundY),
        Obstacles('block', app.gridSize * 317, app.groundY - app.gridSize*4),
        Obstacles('block', app.gridSize * 317, app.groundY - app.gridSize*5),

        Obstacles('spike', app.gridSize * 325, app.groundY),
        Obstacles('block', app.gridSize * 325, app.groundY - app.gridSize*4),
        Obstacles('block', app.gridSize * 325, app.groundY - app.gridSize*5),

        Obstacles('spike', app.gridSize * 329, app.groundY),
        Obstacles('block', app.gridSize * 329, app.groundY - app.gridSize*4),
        Obstacles('block', app.gridSize * 329, app.groundY - app.gridSize*5), 

        Obstacles('spike', app.gridSize * 337, app.groundY),
        Obstacles('block', app.gridSize * 338, app.groundY),
        Obstacles('block', app.gridSize * 342, app.groundY, 2, 1),
        Obstacles('block', app.gridSize * 346, app.groundY, 3, 1),
        Obstacles('block', app.gridSize * 350, app.groundY, 4, 1),
        Obstacles('block', app.gridSize * 351, app.groundY-app.gridSize*(3+2/3),
                  1/3, 4),
        Obstacles('block', app.gridSize * 355, app.groundY-app.gridSize*(2+2/3),
                  1/3, 2),
        Obstacles('block', app.gridSize * 357, app.groundY-app.gridSize*(1+2/3),
                  1/3, 2),
        Obstacles('block', app.gridSize * 359, app.groundY-app.gridSize*(2/3),
                  1/3, 2),
        Obstacles('block', app.gridSize * 362, app.groundY-app.gridSize, 1, 3),
        Obstacles('spike', app.gridSize * 367, app.groundY),
        Obstacles('block', app.gridSize * 367, app.groundY)
        ]
    
def resetLevel(app):
    app.levelStartX = app.width
    app.levelStartY = app.groundY
    app.iconCx = 250
    app.iconCy = app.groundY
    app.iconVelocity = 0
    app.gravity = 0.34
    app.inAir = False
    app.steps = 0

def loadSound(relativePath):
    absolutePath = os.path.abspath(relativePath)
    url = pathlib.Path(absolutePath).as_uri()
    return Sound(url)
      
def redrawAll(app):
    if app.currPage == 0:
        drawHomePage(app)
    else:
        (drawRect(20, 20, 80, 30, fill = None, border = 'white'))
        (drawLabel('< back', 60, 35,size = 15, fill = 'white', 
                   font = 'monospace'))
        if app.currPage == 1:
            (drawRect(0, app.groundY, app.width, app.height - app.groundY, 
                    fill = app.groundColor, border = 'white'))
            drawLevel1(app)
            drawIcon(app, app.iconCx, app.iconCy, 1)
            if app.crashed:
                drawLabel('You Crashed!', app.width/2, 100, size = 40, 
                          fill = 'red', font = 'monospace')
                drawLabel('''Press 'space' to retry''', app.width/2, 145, 
                          size = 25, fill = 'red', font = 'monospace')
        elif app.currPage == 2:
            drawIconEditPage(app)
        elif app.currPage == 3:
            drawHowTo(app)

def drawIcon(app, left, bottom, scale):
    (drawRect(left, bottom, app.gridSize*scale, app.gridSize*scale, 
              fill = app.iconColorOuter, border = 'white' , borderWidth = 0.5,
              align = 'bottom-left')) 
    if app.iconNum == 1:
        (drawRect(left + (app.gridSize*scale)/4, bottom-(app.gridSize*scale)/4, 
                (app.gridSize*scale)/2, (app.gridSize*scale)/2, 
                fill = app.iconColorInner, border = 'white' , borderWidth = 0.5,
                align = 'bottom-left')) 
    elif app.iconNum == 2:
        (drawRect(left + (app.gridSize*scale)/2, bottom-(app.gridSize*scale)/2, 
                  (app.gridSize*scale) * (2**0.5)/2, 
                  (app.gridSize*scale) * (2**0.5)/2, 
                  fill = app.iconColorInner,border = 'white',borderWidth = 0.5,
                  rotateAngle = 45, align = 'center'))
    elif app.iconNum == 3:
        (drawRect(left, bottom, (app.gridSize*scale)/2, (app.gridSize*scale)/2, 
                fill = app.iconColorInner, border = 'white' , borderWidth = 0.5,
                align = 'bottom-left'))
        (drawRect(left + (app.gridSize*scale)/2, bottom-(app.gridSize*scale)/2, 
                  (app.gridSize*scale)/2, (app.gridSize*scale)/2, 
                  fill = app.iconColorInner, 
                  border = 'white' , borderWidth = 0.5, align = 'bottom-left'))

def drawHomePage(app):
    drawLabel('Geometry Dash 112', app.width/2 + 3, app.height/4 + 3, size = 50, 
              fill = 'indigo', font = 'monospace')
    (drawRect(app.width/2 + 3, app.height/2 + 3, 150, 120, fill = None, 
              border = 'indigo', align = 'center'))
    (drawLabel('PLAY', app.width/2 + 3, app.height/2 - 20 + 3, size = 30, 
               fill = 'indigo', font = 'monospace'))
    (drawLabel('LEVEL', app.width/2 + 3, app.height/2 + 20 + 3, size = 30, 
               fill = 'indigo', font = 'monospace'))
    (drawRect(app.width/2 - 100 + 3, app.height/2 + 150 + 3, 150, 80, fill = None, 
              border = 'indigo', align = 'center'))
    (drawRect(app.width/2 + 100 + 3, app.height/2 + 150 + 3, 150, 80, fill = None, 
              border = 'indigo', align = 'center'))
    (drawLabel('Edit Icon', app.width/2 - 100 + 3, app.height/2 + 150 + 3, size = 20, 
               fill = 'indigo', font = 'monospace'))
    (drawLabel('How To', app.width/2 + 100 + 3, app.height/2 + 150 + 3, size = 20, 
               fill = 'indigo', font = 'monospace'))

    drawLabel('Geometry Dash 112', app.width/2, app.height/4, size = 50, 
              fill = 'white', font = 'monospace')
    (drawRect(app.width/2, app.height/2, 150, 120, fill = None, 
              border = 'white', align = 'center'))
    (drawLabel('PLAY', app.width/2, app.height/2 - 20, size = 30, 
               fill = 'white', font = 'monospace'))
    (drawLabel('LEVEL', app.width/2, app.height/2 + 20, size = 30, 
               fill = 'white', font = 'monospace'))
    (drawRect(app.width/2 - 100, app.height/2 + 150, 150, 80, fill = None, 
              border = 'white', align = 'center'))
    (drawRect(app.width/2 + 100, app.height/2 + 150, 150, 80, fill = None, 
              border = 'white', align = 'center'))
    (drawLabel('Edit Icon', app.width/2 - 100, app.height/2 + 150, size = 20, 
               fill = 'white', font = 'monospace'))
    (drawLabel('How To', app.width/2 + 100, app.height/2 + 150, size = 20, 
               fill = 'white', font = 'monospace'))

def drawIconEditPage(app):
    drawLabel('Edit Your Icon', app.width/2, 75, size = 40, 
              fill = 'white', font = 'monospace')
    
    drawLabel('Colors:', 600, 150, size = 25, 
              fill = 'white', font = 'monospace')
    drawLabel('Color 1:', 525, 200, size = 20, 
              fill = 'white', font = 'monospace')
    drawLabel('Color 2:', 675, 200, size = 20, 
              fill = 'white', font = 'monospace')
    
    for i in range(len(app.iconColorList)):
        colorLabel = app.iconColorList[i]
        colorPair = app.iconColorPairs[i]
        colorGradient = gradient(colorPair[0], colorPair[1], start = 'center')
        drawRect(525, 240 + (30*i), 125, 20, fill = colorGradient, 
                 align = 'center')
        drawLabel(colorLabel, 525, 240 + (30*i), size = 15, 
              fill = 'black', font = 'monospace')
        
        drawRect(675, 240 + (30*i), 125, 20, fill = colorGradient, 
                 align = 'center')
        drawLabel(colorLabel, 675, 240 + (30*i), size = 15, 
              fill = 'black', font = 'monospace')
    
    drawLabel('Shapes:', 250, 465, size = 25, 
              fill = 'white', font = 'monospace')
    
    (drawRect(100, 550, app.gridSize, app.gridSize, 
              fill = gradient('dimGray', 'black', start ='center'), 
              border = 'white' , borderWidth = 0.5, align = 'bottom-left'))
    (drawRect(100 + (app.gridSize)/4, 550 - (app.gridSize)/4, 
                (app.gridSize)/2, (app.gridSize)/2, 
                fill = gradient('white', 'silver', start ='center'), 
                border = 'white' , borderWidth = 0.5, align = 'bottom-left'))
    
    
    (drawRect(225, 550, app.gridSize, app.gridSize, 
              fill = gradient('dimGray', 'black', start ='center'), 
              border = 'white' , borderWidth = 0.5, align = 'bottom-left'))
    (drawRect(225 + (app.gridSize)/2, 550 - (app.gridSize)/2, 
                  (app.gridSize) * (2**0.5)/2, (app.gridSize) * (2**0.5)/2, 
                  fill = gradient('white', 'silver', start ='center'),
                  border = 'white',borderWidth = 0.5, rotateAngle = 45, 
                  align = 'center'))
    
    
    (drawRect(350, 550, app.gridSize, app.gridSize, 
              fill = gradient('dimGray', 'black', start ='center'), 
              border = 'white' , borderWidth = 0.5, align = 'bottom-left'))
    (drawRect(350, 550, (app.gridSize)/2, (app.gridSize)/2, 
                fill = gradient('white', 'silver', start ='center'), 
                border = 'white' , borderWidth = 0.5, align = 'bottom-left'))
    (drawRect(350 + (app.gridSize)/2, 550 - (app.gridSize)/2, 
                  (app.gridSize)/2, (app.gridSize)/2, 
                  fill = gradient('white', 'silver', start ='center'), 
                  border = 'white' , borderWidth = 0.5, align = 'bottom-left'))

    drawIcon(app, 150, 400, 4)

def drawHowTo(app):
    (drawLabel('How To Play', app.width/2, 50, size = 40, 
                font = 'monospace', fill = 'white'))
    (drawLabel('Travel Through The Level', app.width/2, 125, size = 25, 
                font = 'monospace', fill = 'white'))
    drawLine(app.width/2 - 150, 250, app.width/2 + 150, 250, 
             fill = 'white')
    drawRect(app.width/2 - 110, 220, 30, 30, fill = 'white', border = 'white')
    drawPolygon(app.width/2 - 20, 250, app.width/2 - 5, 220, 
                app.width/2 + 10, 250, fill = 'white', border = 'white')
    drawPolygon(app.width/2 + 10, 250, app.width/2 + 25, 220, 
                app.width/2 + 40, 250, fill = 'white', border = 'white')
    drawPolygon(app.width/2 + 40, 250, app.width/2 + 55, 220, 
                app.width/2 + 70, 250, fill = 'white', border = 'white')

    (drawLabel('''Press 'Space' To Jump''', app.width/2, app.height/2,size = 25, 
                font = 'monospace', fill = 'white'))
    drawLine(app.width/2 - 150, app.height/2 + 125, app.width/2 + 150, 
             app.height/2 + 125, fill = 'white')
    drawRect(app.width/2 + 5, app.height/2 + 40, 30, 30, fill = 'white', border = 'white')
    drawPolygon(app.width/2 - 20, app.height/2 + 125, app.width/2 - 5, app.height/2 + 95, 
                app.width/2 + 10, app.height/2 + 125, fill = 'white', border = 'white')
    drawPolygon(app.width/2 + 10, app.height/2 + 125, app.width/2 + 25, app.height/2 + 95, 
                app.width/2 + 40, app.height/2 + 125, fill = 'white', border = 'white')
    drawPolygon(app.width/2 + 40, app.height/2 + 125, app.width/2 + 55, app.height/2 + 95, 
                app.width/2 + 70, app.height/2 + 125, fill = 'white', border = 'white')

    (drawLabel('And Have Fun!', app.width/2, app.height - 100,size = 25, 
                font = 'monospace', fill = 'white'))

def drawLevel1(app):
    (drawLabel('Level 1', app.levelStartX - app.width/2, 175, 
              fill = 'white', size = 40, font = 'monospace'))
    for i in range(len(app.level1Obstacles)):
        drawObstacle(app, app.level1Obstacles[i])

def drawObstacle(app, obstacle):
    vtxsCopy = copy.copy(obstacle.vtxs)
    for i in range(0, len(vtxsCopy), 2):
        vtxsCopy[i] += app.levelStartX
    drawPolygon(*vtxsCopy, fill = app.obstacleColor, border = 'white')

def setColors(app):
    if app.currPage == 0:
        app.background = gradient('darkMagenta', 'indigo', start = 'center')
    if app.currPage == 1:
        if app.steps < 3000:
            app.background = gradient('cyan', 'mediumBlue', start = 'top')
            app.obstacleColor = gradient('dodgerBlue', 'navy', start = 'top')
            app.groundColor = gradient('midnightBlue', 'blue', start = 'top')
        if app.steps > 3120:
            app.background = gradient('salmon', 'red', start = 'top')
            app.obstacleColor = gradient('fireBrick', 'black', start = 'top')
            app.groundColor = gradient('darkRed', 'red', start = 'top')

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
        if ((app.width/2 - 75 <= mouseX <= app.width/2 + 75) and 
            (app.height/2 - 60 <= mouseY <= app.height/2 + 60)):
            app.currPage = 1
            app.level1Music.play(restart = True)
            app.menuMusic.pause()
        elif ((app.width/2 - 175 <= mouseX <= app.width/2 -25) and 
            (app.height/2 + 110 <= mouseY <= app.height/2 + 190)):
            app.currPage = 2
        elif ((app.width/2 + 25 <= mouseX <= app.width/2 + 175) and 
            (app.height/2 + 110 <= mouseY <= app.height/2 + 190)):
            app.currPage = 3
    else:
        if (20 <= mouseX <= 100) and (20 <= mouseY <= 50):
            if app.currPage == 1:
                app.level1Music.pause()
                app.menuMusic.play(restart = True, loop = True)
            app.currPage = 0
            resetLevel(app)
        elif app.currPage == 2:
            if (500 <= mouseY <= 550):
                if (100 <= mouseX <= 150):
                    app.iconNum = 1
                elif (225 <= mouseX <= 275):
                    app.iconNum = 2
                elif (350 <= mouseX <= 400):
                    app.iconNum = 3
            if (462.5 <= mouseX <= 587.5):
                for i in range(len(app.iconColorList)):
                    if 225 + (30*i) <= mouseY <= 255 + (30 * i):
                        colorPair = app.iconColorPairs[i]
                        colorGradient = gradient(colorPair[0], colorPair[1], 
                                                start = 'center')
                        app.iconColorOuter = colorGradient
            elif (612.5 <= mouseX <= 737.5):
                for i in range(len(app.iconColorList)):
                    if 225 + (30*i) <= mouseY <= 255 + (30 * i):
                        colorPair = app.iconColorPairs[i]
                        colorGradient = gradient(colorPair[0], colorPair[1], 
                                                start = 'center')
                        app.iconColorInner = colorGradient

def onKeyPress(app, key):
    if app.currPage == 1:
        if key == 'space':
            if not (checkCollision(app, app.level1Obstacles) or app.inAir):
                app.inAir = True
                app.iconVelocity = -9
            if checkCollision(app, app.level1Obstacles):
                resetLevel(app)
                app.level1Music.play(restart = True)
                

def onKeyHold(app, keys):
    if 'space' in keys:
        if not (checkCollision(app, app.level1Obstacles) or app.inAir):
                app.inAir = True
                app.iconVelocity = -9
        if app.crashed:
            app.crashed = False
                
def onStep(app):
    setColors(app)
    if app.currPage == 1:
        if not checkCollision(app, app.level1Obstacles):
            app.levelStartX -= 4.25
            app.steps += 1
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
            app.crashed = True
            app.level1Music.pause()

def main():
    runApp()

main()