class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price 
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if (price > 10000):
            self.tax = .15
        else:
            self.tax = .12

    def display_all(self):
        print "Price: {}".format(self.price)
        print "Speed: {}".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {}".format(self.mileage)
        print "Tax: {}".format(self.tax)
        return self
    
c1 = Car(2000, "35mph", "Full", "15mpg").display_all()
print c1
c2 = Car(2000, "5mph", "Not Full", "105mpg").display_all()  
c3 = Car(2000, "15mph", "Kind of Full", "95mpg").display_all()  
c4 = Car(2000, "25mph", "Full", "25mpg").display_all()  
c5 = Car(2000, "45mph", "Empty", "25mpg").display_all()  
c6 = Car(200000000, "35mph", "Empty", "15mpg").display_all()  