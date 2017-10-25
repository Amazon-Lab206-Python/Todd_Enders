def make_tuples(obj):
    return obj.items()

def make_tuples2(obj):
    new_list = []
    for key,val in obj.items():
        tup = (key, val)
        new_list.append(tup)
    return new_list 

def make_tuples3(obj):
    new_list = []
    for key in obj:
        tup = (key, obj[key])
        new_list.append(tup)
    return new_list

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

print make_tuples(my_dict)