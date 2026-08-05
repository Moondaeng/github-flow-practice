class Work():
    def __init__(self, human):
        self.human = human
    
    def working(self, human):
        if self.human > human:
            self.human -= human
        else:
            self.human = 0
        