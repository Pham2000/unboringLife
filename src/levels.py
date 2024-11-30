class Level:
    #current level
    current = 0
    #tasks
    xp = 0 
    
    #default constructor
    def __init__(self):
        self.current = 0
        self.xp = 0.0

    #setting level
    def setLevel(self, current):
        self.current = current

    #getting level
    def getLevel(self):
        return self.current

    #setting xp
    def setXp(self, xp):
        self.xp = xp

    #getting xp
    def getXp(self):
        return self.xp

    #Xp requirement for leveling up
    def getXpRequirement(self):
        return self.current + 87 * self.current + 100
    
    #getting ranks
    def getTier(self):
        if self.current <= 10:
            return "F"
        elif self.current >= 11 and self.current <= 20:
            return "E"
        elif self.current >= 21 and self.current <= 40:
            return "D"
        elif self.current >= 41 and self.current <= 65:
            return "C"
        elif self.current >= 66 and self.current <= 82:
            return "B"
        elif self.current >= 83 and self.current <= 104:
            return "A"
        elif self.current >= 105 and self.current <= 125:
            return "S"
        else:
            return "S+"
        
        

    





    



