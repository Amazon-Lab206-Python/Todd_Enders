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