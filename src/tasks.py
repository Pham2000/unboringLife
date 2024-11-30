#taks

class Task:
    #the tasks
    theTasks = {}

    #default constructor of tasks
    def __init__(self):
        self.theTasks = {}

    #setting tasks
    def addingTasks(self, t, xp):
        self.theTasks[t] = xp

    #print tasks
    def printTasks(self):
        print(list(self.theTasks))

    #get tasks
    def getTasks(self):
        return self.theTasks
    

    
