import random

def fizzbuzz(num):
    for i in range(num):
        # print i
        return i


# print fizzbuzz(20)

myinfo = {
    'name': 'Felix',
    'location': 'Seattle',
    'hobbies': 'Mispronouncing tech jargon'
}

myinfo['name'] = 'Felix Chawesome'
myinfo.items() # [('name', 'Felix'), ('location', 'Seattle'), ('hobbies', 'tech jargon')]
# for key,val in x: # for whatever in a list
#     print key, val

#basic, always works-level
# for key in myinfo:
#     print key, myinfo[key]

# #advanced
# for key, val in myinfo.items():
#     print key, val

# score = input("What's the score?")
# print score

for row in range(8):
    checker_str = ""
    for col in range(8):
        if (row % 2 == 0 and col % 2 == 0):
            checker_str += "*"
        elif (row % 2 == 0 and col % 2 == 1):
            checker_str += " "
        elif (row % 2 == 1 and col % 2 == 1):
            checker_str += "*"
        else:
            checker_str += " "
    print checker_str
