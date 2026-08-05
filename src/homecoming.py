class HomeComing():
    words = "집에가는사람"

    def __init__(self):
        self.energy = 10

    def go_home(self, energy):
        if energy == 10:
            print(self.words)
        
        self.energy += 10
        
        return self.energy

    

        