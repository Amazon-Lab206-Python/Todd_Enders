ml = ['magical unicorns',19,'hello',98,'world']
il = [2,3,1,7,4,12]
sl = ['magical','unicorns']

testlist = sl 
sum = 0
phrase = ""
listtype = None

for val in testlist:
    if (type(val) is int):
        sum += val 
        if (listtype is "string"):
            listtype = "mixed"
        elif (listtype is None):
            listtype = "integer"
    else:
        phrase += val 
        if (listtype is "integer"):
            listtype = "mixed"
        elif (listtype is None):
            listtype = "string"

print "The list you entered is of {} type".format(listtype)

if (listtype is "integer" or listtype is "mixed"):
    print "Sum: {}".format(sum)
if (listtype is "string" or listtype is "mixed"):
    print "String: {}".format(phrase)


