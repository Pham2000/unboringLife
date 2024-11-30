class Task:
    #the tasks
    theTasks = {}
    #ranking of tasks
    priority = {}

    #default constructor of tasks
    def __init__(self):
        self.theTasks = {}
        self.priority = {}

    #setting tasks
    def addingTasks(self, t):
        self.theTasks += t

    #setting priority
    def addingPriority(self, p):
        self.priority += p

    #print tasks
    def printTasks(self):
        print(self.theTasks)

    #print priority
    def printPriority(self):
        print(self.priority)

    #mapping tasks with priority and return it
    def mapTP(self):
        return dict(zip(self.theTasks, self.priority))
    

    
