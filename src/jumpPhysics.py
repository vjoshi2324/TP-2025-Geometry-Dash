class jumpPhysics:
    def __init__(self, initialVelocity, gravity, cy, ground):
        self.initialVelocity = initialVelocity
        self.gravity = gravity
        self.cy= cy
        self.velocity = 0
        self.time = 0
        self.ground = ground

    def takeJump(self, dt):
        self.time += dt
        self.velocity = self.initialVelocity + self.gravity * self.time
        self.cy = ((self.initialVelocity * self.time) + 
                    (0.5 * self.gravity * (self.time ** 2)))
        if self.cy > self.ground:
            self.cy = self.ground
            self.velocity = 0

    def resetVals(self):
        self.time = 0
        self.cy = self.ground
        self.velocity = 0