class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "Price: {}, Max Speed: {}, Miles: {}".format(self.price, self.max_speed, self.miles)
        return self 

    def ride(self):
        print "Riding"
        self.miles += 10 
        return self
    
    def reverse(self):
        print "Reversing"
        if (self.miles - 5 >= 0):
            self.miles -= 5
        return self 

b1 = Bike(99.99, "20mph")
b2 = Bike(999.99, "30mph")
b3 = Bike(1999.99, "50mph")

b1.ride().ride().ride().reverse().displayInfo()
b2.ride().ride().reverse().reverse().displayInfo()
b3.reverse().reverse().reverse().displayInfo()


    