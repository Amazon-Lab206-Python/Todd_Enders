# Author: Todd Enders October 2017
# Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"

print words.find("day")

newwords = words.replace("day", "month")

print newwords

# Min and Max
x = [2,54,-2,7,12,98]

print min(x), max(x)

# First and Last
y = ["hello",2,54,-2,7,12,98,"world"]

print y[0], y[len(y)-1]

z = list()
z.append(y[0])
z.append(y[len(y)-1])
print z

# New List

a = [19,2,54,-2,7,12,98,32,10,-3,6]
a.sort()

print a
first_list = a[:len(a)/2] # optional first parameter of slice defaults to zero
second_list = a[len(a)/2:] # optional second parameter of slice defaults to the list's length
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list
# innerlist = list()
# outerlist = list()

# for i in range(0, len(a)/2):
#     innerlist.append(a[i])

# outerlist.append(innerlist)
# for i in range(len(a)/2, len(a)):
#     outerlist.append(a[i])

# print outerlist

