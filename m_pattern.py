for row in range (6):
    for col in range (7):
        if (col==0) or (col==6) or (col-row==0 and col<4) or (col>3 and col+row==6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    