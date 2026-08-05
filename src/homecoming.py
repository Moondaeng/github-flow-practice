class HomeComing():
    words = "집에가는사람"

    def __init__(self,energy=10):
        self.energy = energy

    def go_home(self):
        if self.energy == 10:
            print(self.words)
        
        self.energy += 10
        
        return self.energy

    

        