class MathDojo(object):
    def __init__(self):
        self.result = 0 

    def add(self, *nums):
        for obj in nums:
            if type(obj) is list or type(obj) is tuple:
                for num in obj:
                    self.result += num
            else:
                self.result += obj 
        return self 

    def subtract(self, *nums):
        for obj in nums:
            if type(obj) is list or type(obj) is tuple:
                for num in obj:
                    self.result -= num
            else:
                self.result -= obj
        return self 

md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).result
print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
