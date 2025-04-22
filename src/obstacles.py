class Obstacles:
    def __init__(self, type, leftX, bottomY, gridSize):
        self.type = type
        self.leftX = leftX
        self.bottomY = bottomY
        self.gridSize = gridSize

    def obstacleSpecs(self):
        if self.type == 'block':
            vtxs = ([self.leftX, self.bottomY, self.leftX, 
                     self.bottomY - self.gridSize, self.leftX + self.gridSize, 
                     self.bottomY - self.gridSize, self.leftX + self.gridSize, 
                     self.bottomY])
        elif self.type == 'flat spike':
            vtxs = ([self.leftX, self.bottomY, self.leftX + self.gridSize/2, 
                     self.bottomY - self.gridSize/3, self.leftX + self.gridSize, 
                     self.bottomY])
        elif self.type == 'spike':
            vtxs = ([self.leftX, self.bottomY, self.leftX + self.gridSize/2, 
                     self.bottomY - self.gridSize, self.leftX + self.gridSize, 
                     self.bottomY])


