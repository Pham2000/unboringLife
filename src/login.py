#might use later

class Login:
    
    #username
    username = ""
    #password
    password = ""

    #constructor
    def __init__(self, username, password):
        self.username = username
        self.password = password

    #setting username
    def setUser(self, username):
        self.username = username

    #setting password
    def setPassword(self, password):
        self.password = password

    #getting username
    def getUser(self):
        return self.username
    
    #getting password
    def getPassword(self):
        return self.password
    


    