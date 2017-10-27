import datetime

class Call(object):
    id_counter = 0
    
    def __init__(self, name, number, reason):
        self.name = name 
        self.number = number
        self.reason = reason 
        self.time = datetime.datetime.now()
        Call.id_counter += 1
        self.id = Call.id_counter

    def display(self):
        print "Call name: {}".format(self.name)
        print "Call reason: {}".format(self.reason)
        print "Call number: {}".format(self.number)
        print "Call time: {}".format(self.time)
        print "Call id: {}".format(self.id)
        print "============="

class CallCenter(object):
    def __init__(self):
        self.call_list = []
        self.queue_size = 0
    
    def add(self, call):
        self.call_list.append(call)
        self.queue_size += 1
        return self

    def remove(self):
        if (self.queue_size):
            self.call_list.pop(0)
            self.queue_size -= 1
        return self

    def info(self):
        for call in self.call_list:
            call.display()
        print self.queue_size


c1 = Call("Todd", "555-1212", "I need help troubleshooting")
c2 = Call("Jayme", "555-1212", "I need help coding things")

cc1 = CallCenter()
cc1.add(c1)
cc1.add(c2)

cc1.info()

# c1.display()
# c2.display()
