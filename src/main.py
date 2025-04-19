from cmu_graphics import *

def onAppStart(app):
    app.width = 800
    app.height = 600
    app.sqSize = 200

def redrawAll(app):
    cx, cy = app.width/2, app.height/2
    drawRect(cx, cy, app.sqSize, app.sqSize)

def main():
    runApp()

main()