# x = 10
# for i in range(0, x):
#     print i

# tuples (1,2,3)

x = (1,2,3)

# dictionary {}

obj = {
    'mykeys': "boo"
}

print obj['mykeys']

# strings 

word = "this thing"
capword = word.capitalize()
print capword

phrase = "Hello World, love {}, PS - {} is awesome".format("Noah", "Negative Margin Man")
print phrase

# boolean
booly = True
booly = False
booly = None

# integers
z = 10 

# floats
a = 1.11111113

print type(a)

# lists
y = [0, "a", "b", "c"]
print len(obj)

if (len(y) > 2):
    print "Yahoo!"
elif (len(y) >= 1):
    print "Yah"
else:
    print "Sad"

for i in range(0,len(y)):
    print y[i]

for key in obj:
    print obj[key]