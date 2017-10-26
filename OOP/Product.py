class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price 
        self.name = name 
        self.weight = weight 
        self.brand = brand 
        self.status = "For Sale"

    def sell(self):
        self.status = "Sold"
        return self 

    def add_tax(self, tax):
        return self.price + (self.price * tax)

    def return_product(self, reason):
        if (reason == "defective"):
            self.status = "Defective"
            self.price = 0
        elif (reason == "returned in box"):
            self.status = "For Sale"
        elif (reason == "opened"):
            self.status = "Used"
            self.price = self.price - (self.price * .2)
        return self

    def display_info(self):
        print "Price: {}".format(self.price)
        print "Name: {}".format(self.name)
        print "Weight: {}".format(self.weight)
        print "Brand: {}".format(self.brand)
        print "Status: {}".format(self.status)
        print "==========="
        return self

p1 = Product(99.99, "Cell phone", "6 oz", "Samsung")
p2 = Product(299.99, "PS4", "5 lbs", "Sony")
p3 = Product(399.99, "XBox One", "6 lbs", "Microsoft")
p1.return_product("defective").display_info()
p2.return_product("returned in box").display_info()
p3.return_product("opened").display_info()
