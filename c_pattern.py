for row in range(5):
    for col in range(5):
        if row==0 and col!=0 or row==4 and col!=0 or col==0 and row!=0 and row!=4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()