def drawstars(num_list):
    for num in num_list: #outer for loop moving through the num_list numbers
        star_string = ""
        for i in range(num): #inner for loop printing NUM stars
            star_string += "*"
        
        print star_string
        


drawstars([4, 6, 1, 3, 5, 7, 25])