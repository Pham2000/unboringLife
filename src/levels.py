class Level:
    #current level
    current = 0
    #tasks
    xp = 0
    
    #default constructor
    def __init__(self):
        self.currentLevel = 0
        self.xp = 0.0

    #setting level
    def setLevel(self, current):
        self.current = current

    #getting level
    def getLevel(self):
        return self.current

    #setting tasks
    def setTasks(self, xp):
        self.xp = xp

    #getting tasks
    def getTasks(self):
        return self.xp

    





    



