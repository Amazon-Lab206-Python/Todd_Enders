def odd_even():
    for num in range(2001):
        if (num % 2 is 0):
            print "Number is {}. This is an even number".format(num)
        else:
            print "Number is {}. This is an odd number".format(num)

# odd_even()

def multiply(incoming_list):
    new_list = []
    for value in incoming_list:
        new_list.append(value*5)
    return new_list

the_list = [1,2,3,4,5,6]
# print multiply(the_list)

def multiply_with(incoming_list, factor):
    new_list = []
    for value in incoming_list:
        new_list.append(value*factor)
    return new_list

# print multiply_with(the_list, 10)

