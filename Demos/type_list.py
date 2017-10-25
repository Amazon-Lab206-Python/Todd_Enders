l1 = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical','unicorns']

test = l3
sum = 0
str_hits = 0
num_hits = 0
phrase = ""
for val in test: # iterating through the values in the list
    if (type(val) is str): # check if value is of type str
        str_hits += 1
        phrase += val + " "
    elif (type(val) is int or float): # check if value is of type int
        num_hits += 1
        sum += val 

if (str_hits and num_hits):
    print "mixed type"
    print "the string is: {}".format(phrase)
    print "sum: {}".format(sum)
elif (str_hits):
    print "string type"
    print "the string is: {}".format(phrase)
else:
    print "integer type"
    print "sum: {}".format(sum)

