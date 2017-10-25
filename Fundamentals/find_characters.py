# Author Todd Enders October 2017

word_list = ['hello','world','my','name','is','Anna']
char = 'o'

found_list = list()
for word in word_list:
    if (word.find(char) >= 0):
        found_list.append(word)

print found_list