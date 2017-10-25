# Odd numbers from 1 to 1000
# for i in range(1,1001):
    # print i

# Multiples of 5 from 5 to 1000000
# for i in range(5, 1000001, 5):
#     print i

# Sum this list a = [1, 2, 5, 10, 255, 3]
# a = [1, 2, 5, 10, 255, 3]
# print sum(a)

# Print the average of this list a = [1, 2, 5, 10, 255, 3]

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in range(0, len(a)):
    sum += a[i]
print sum/len(a)