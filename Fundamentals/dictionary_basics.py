me = {
    'name': 'Todd',
    'age': 33,
    'country of birth': 'United Kingdom',
    'favorite language': 'Python'
}

def print_me(obj):
    for key,val in obj.items():
        print "My {} is {}".format(key, val)

print_me(me)