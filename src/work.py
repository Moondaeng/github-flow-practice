class Work():
    def __init__(self, energy):
        self.energy = energy
    
    def working(self, energy):
        if self.energy > energy:
            self.energy -= energy
        else:
            self.energy = 0
        
        return self.energy