class Person(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def talk(self, phrase):
        print phrase
        return self
    
    def code(self):
        print "I've been coding for {} years".format(self.age)
        return self

p1 = Person(33, "Todd")
p2 = Person(1.7, "Noah")
p3 = Person(10, "Dennis The Menace")

p1.talk("I'm the instructor").code().talk("what's up").code()
# p2.talk("I'm happy to be here")
# p3.talk("Mr. Wilson")

# p1.code()
# p2.code()
# p3.code()


# "hello".capitalize()

# "world".capitalize()

# class str(object):
#     def capitalize(self):
