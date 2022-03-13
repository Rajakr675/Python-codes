# for row in range (7):
#     for col in range (4):
#         if (row==0) or (col==0) or (row==3 and col!=3) :
#             print("*",end="")
#         else:
#             print(end="")
#     print()

# for row in range (5):
#     for col in range (5):
#         if (row==0) or (row==4) or (row+col==4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# .....febonacci seris......#
# n=int(input("enter"))
# x=0
# y=1
# z=0
# while z<n :
#     print(z)
#     x=y
#     y=z
#     z=x+y


#.......pattern print....#
# 1
# 22
# 333
# 4444..............

# n=int(input("entr"))
# i=1
# for i in range (1,n):
#     print(str(i)*i)

#  passcal traingle ..............................


# p=int(input("enter the number"))
# for i in range(1,p+1):
#     for j in range(0,p):
#         print("",end="")
#     c=1
#     for j in range (1,i+1):
#         print("",c,end=" ")
#         c=c*(i-j)//j
#     print()
        

# snack pattern.............................................
# a = 1
# b= int(input('Enter any No.: '))
# for i in range(1,b+1):
#     if i%2 != 0:
#         for j in range(b):
#             if a<10:
#                 print(a,end="  ")
#             else:
#                 print(a,end=" ")
#             a+=1
#     if i%2==0:
#         for j in range(a+b-1,a-1,-1):
#             if a<10:
#                 print(j,end="  ")
#             else:
#                 print(j,end=" ")
#             a+=1

#     print()

# how to count value.

# a=int(input("enter"))
# c=0
# while a>0:
#     y=a%10
#     c+=1
#     a=a//10
# print(c)

#  water level question
# a=int(input('enter'))
# if a>=0 and a<33:
#     print('low water level')
# elif a>=66 and a<99:
#     print('middle level')
# else:
#     print('over water level')
    