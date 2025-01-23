# man.py
# Initializing class and creating methods and

class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")


m = Man("Woody")
m.hello()
m.goodbye()
