class Obstacles:
    def __init__(self, type, leftX, bottomY, height = 1, width = 1):
        self.type = type
        self.leftX = leftX
        self.bottomY = bottomY
        self.gridSize = 50
        self.height = height
        self.width = width
        self.vtxs = []
        self.blockVtxs = []
        if self.type == 'block':
            self.vtxs = ([self.leftX, self.bottomY, 
                          self.leftX, self.bottomY - self.gridSize*self.height, 
                          self.leftX + self.gridSize * self.width, 
                          self.bottomY - self.gridSize * self.height, 
                          self.leftX + self.gridSize*self.width, self.bottomY])
        elif self.type == 'flat spike':
            self.vtxs = ([self.leftX, self.bottomY, 
                          self.leftX + self.gridSize/2, 
                          self.bottomY - self.gridSize/3, 
                          self.leftX + self.gridSize, self.bottomY])
        elif self.type == 'spike':
            self.vtxs = ([self.leftX, self.bottomY, 
                          self.leftX+self.gridSize/2,self.bottomY-self.gridSize, 
                          self.leftX + self.gridSize, self.bottomY])
        elif self.type == 'flat block':
            self.vtxs = ([self.leftX, self.bottomY - self.gridSize * (2/3), 
                          self.leftX, self.bottomY - self.gridSize, 
                          self.leftX+self.gridSize, self.bottomY-self.gridSize, 
                          self.leftX + self.gridSize, 
                          self.bottomY - self.gridSize * (2/3)])
            
            
    def __eq__(self, other):
        return ((self.type == other.type) and (self.leftX == other.leftX) and
                (self.bottomY == other.bottomY))
    
    def __hash__(self):
        return hash(str(self))



