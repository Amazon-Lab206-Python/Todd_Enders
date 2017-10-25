def dict_maker(list1, list2):
    new_dict = {} 
    for idx in range(len(list1)):
        new_dict[list1[idx]] = list2[idx]

    return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print dict_maker(name, favorite_animal)

def dict_maker_hacker(list1, list2):
    new_dict = {}
    longer_list = list1 
    shorter_list = list2
    if (len(list2) > len(list1)):
        longer_list = list2 
        shorter_list = list1
    for idx in range(len(longer_list)):
        if (idx < len(shorter_list)):
            new_dict[longer_list[idx]] = shorter_list[idx]
        else:
            new_dict[longer_list[idx]] = None
    
    return new_dict 

name2 = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "Todd"]
favorite_animal2 = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print dict_maker_hacker(name2, favorite_animal2)