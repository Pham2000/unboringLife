import time
from src.levels import Level
from src.login import Login
from src.tasks import Task


level = Level()
i = 1
g = 1
while g < 10:
    level.setXp(i)
    
    if level.xp >= level.getXpRequirement():
        i = 0
        level.setLevel(g)
        level.setXp(i)
        g+=1
        
    
    print("current xp: " + str(level.getXp()) + " Level: " + str(level.getLevel()))
    i+=1
    time.sleep(0.03)