def drawstars(num_list):
    for num in num_list: #outer for loop moving through the num_list numbers
        star_string = ""
        for i in range(num): #inner for loop printing NUM stars
            star_string += "*"
        
        print star_string
        
# drawstars([4, 6, 1, 3, 5, 7, 25])

def drawthings(mixed_list):
    for value in mixed_list:
        if (type(value) is int):
            star_string = ""
            for i in range(value): #inner for loop printing NUM stars
                star_string += "*"
            print star_string
        else:
            char_string = ""
            first_char = value[0].lower()
            for times in range(len(value)):
                char_string += first_char 
            print char_string 

drawthings([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])