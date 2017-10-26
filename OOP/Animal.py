class Animal(object):
    def __init__(self, name):
        self.name = name 
        self.health = 100
    
    def walk(self):
        self.health -= 1
        return self 

    def run(self):
        self.health -= 5
        return self 

    def display_health(self): 
        print "Health: {}".format(self.health)
        return self 

a1 = Animal("Fluffy")
a1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    
    def pet(self):
        self.health += 5
        return self 

d1 = Dog("Scruffy")
d1.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    
    def fly(self):
        self.health -= 10
        return self
    
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"
        return self


dr1 = Dragon("Toothless")
dr1.fly().fly().display_health()

    