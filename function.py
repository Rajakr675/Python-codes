# def my_function():
#   print("Hello from a function")

# my_function()def my_function(fname):

# 2ed example
# def addition(a,b):
#     c=a+b
#     print("addition=",c)
# addition(5,10)


# ...function meraki question..................................#
# for example

# def text():

#     print('my name is raja ')
# print('what is your name')
# text()


# ..1).function question..1

# def raja():
#     print("Who is the founder of Facebook?")
#     print("Mark Zuckerberg")
#     print("bill gates")
#     print("steve jobs")
#     print("larry")

# raja()
# raja()
# raja()
# raja()
# raja()

# ..1).. question

# def raja():
#     print("*)Who is the founder of Facebook?")
#     print("a)Mark Zuckerberg")
#     print("b)bill gates")
#     print("c)steve jobs")
#     print("dlarry")    
# b=1
# while b<=100:
#     raja()
#     b+=1


# Question...1 in meraki.You have to print the largest value out of the given list using the max function.

# def my_numbers(n):
#     r = max(n)
#     print(r)
    


# numbers = [3, 5, 7, 34,45678, 2, 89, 2, 5]
# my_numbers(numbers)

# # ..2)question()ou have to print the sum of the elements of the given list by using the sum function.
# def sum(x):
#     x=0
#     for i in numbers:
#         x+=i
#     print(x)

# numbers = [1, 2, 3, 4, 5]
# sum(numbers)


# ..3).question..Using sort function sort the given list.

# def sort_number():
#     x=sorted(list)
#     print(x)


# list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# sort_number()

# ..Q4. By using reverse function print the reverse order of the list.


# def reverse_list():
#     x=[]
#     for i in range (1,len(list)+1):
#         x.append(list[-i])
#     print(x)


# list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# reverse_list()


# ..Q5. Use the min function and find the minimun value of the list.

# def  min_number(n):
#     x=min(n)
#     print(x)


# list = [8, 6, 4, 8, 4, 50, 2, 7]
# min_number(list)


# ..Debug Code.....
# def sum():
#     print(12+13)
# sum()

# ....Debug Code...........#

# def welcome():
#     print("Welcome to function")
# welcome()

# ....Debug Code...........#

# def isEven():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number")
# isEven()




# ...functions-args.....question..1)

# def max_number(n):
#     x=max(n)
#     print(x)
# list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
# max_number(list)


# ..functions-args.....question..2)e use the len( )
#  function to find the length of an array or sequence. It is al
# def lent_num(n):
#     x=len(n)
#     print(x)
# a=[1,2,3,4,5,6]
# lent_num(a)




# note informition...................
                
# paramiters
# arguements
# function
# defolt_paramiters
# global_values
# 
# ...................................
# ...3)question..

# def say_hello(name):
#     print("Hello ", name)
#     print("How are you?")
# say_hello("Aatif")

# .......

# ...code debug  :1).question......................#

# def greet(names):
#     for name in names:
#         print("Welcome", name)

# a="Rinki", "Vishal", "Kartik", "Bijender"
# greet(a)


# ...Question 2)..

# def info(name, age = 5):
#    print(name + " is " + str(age) + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")

# ...3.)question.....

# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


# studentDetails("Nilam","loop","raja")



# functions-question  2.)...

#  write your function here

# def name(n):
#     print(n)
# a=("My name is Rishabh.\ni am the co-founder of NavGurukul.")
# name(a)

#  -output 
# My name is Rishabh..
# I am the co-founder of NavGurukul.

# question.2)..Question 3 (Part 1) in meraki 

# def func(n):
#     print(list(n))

# stud=("RAJA","bhumeh","akash","praveen")
# func(stud)

# ..Question 3 (Part 2).....#You have to define a function named isGreaterThan20 
# in which you have to pass two parameters to the function and the first parameter 
# by default should be 20.................................


# def is_greterthan(a,b=20):
#     print(a)
#     print(b)
# a=45
# is_greterthan(a)



# functions-question3..[functions-question part 1]..universal addition in function

# def add_num(a,b):
    
#     x=a+b
#     print(x)
# a=int(input('enter'))
# b=int(input("enter"))
# add_num(a,b)


# Question (Part 2) in meraki ....


# def add_numbers_list (n):
#     a,c=b
#     for i in range (len(c)):
#         m=a[i]+c[i]
#         print(m)
# b=[50, 60, 10],[10, 20, 13] 
# add_numbers_list (b)


# # ....Question  1.....

# def voter(n):
#     if a>=age:
#         print("you eligibal")
#     else:
#         print("you not eligibal")
                

# a=int(input("enter"))
# age=18
# voter(age)

#  question..2 perfect   number in' function...

# def perfect_num(n):
#     b=0
#     for i in range (1,a):
#         if a%i==0 :
#             b=b+i
#     if b==a:
#         print(a,"is a perfect number ")
#     else:
#         print(a,"is not perfect number ")

# a=int(input("enter"))
# perfect_num(a)

# ,,question...3................Create a function which takes 3 arguments(all integers) and prints their sum and average as shown below.
# 1st type

# def average_num_add(a,b,c):
#     d=a+b+c
#     e=d//3
#     print(d)
#     print(e)


# a=int(input("enter"))
# b=int(input("enter"))
# c=int(input("enter"))
# ...............................Create a function which takes 3 arguments(all integers) and prints their sum and average as shown below.
# 2ed type
# average_num_add(a,b,c)

# def ave_add_num():
#     b=0
#     for i in range (10):
#         a=int(input("enter the number:"))
#         b+=a
#     print("your sum is ",b)
#     print("your average is ",b//i)
    
# ave_add_num()


# question.....4
# def odd_even_num():
#     a=int(input("enter"))
#     for i in range (a):
#         if i %2==0:
#             print("even",i)
#         else:
#             print("odd",i)

# odd_even_num()

# question....1).   # Python functions ..find the Max of three numbers...........w3 resource.....................#

# def f():
#     if n1>=n2 and n1>=n3:
#         m=n1
#     elif n2>=n1 and n2>=n3:
#         m=n2
#     else:
#          m=n3
#     print("Largest number among  the three is",m)
# n1=int(input("Enter first number: "))

# n2=int(input("Enter second number: "))

# n3=int(input("Enter Third number: "))

# f()


# ....question..2)..function to sum all the numbers in a list...

# def sum_list():
#     a=[4,3,5,0]
#     b=0
#     for i in a:
#         b+=i
#     print(b)
# sum_list()

# # ..question.3)..multiply all the numbers in a list. 
# def multipal_list():
#     a=[4,5,-1,2]
#     b=1
#     for i in a:
#         b*=i
#     print(b)
# multipal_list()

# ...question..4)..Python program to reverse a string. 

# def reverce_str():
#     a="1234abcd"
#     print(a[::-1])
# reverce_str()
    

# ...quetion...5)



# ...question..6)..check whether a number falls in a given range.

# def test_range(n):
#     if n in range(4,16):
#         print( " %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(8)

# ..question...7)..



# ..question..8).

# def only_real_val(a):
#     b=[]
#     for i in a:
#         if i not in b:
#             b.append(i)
#     print(b)

# a=[1,2,3,3,3,3,4,5]
# only_real_val(a)
    
# ..question..9)...
# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True             
# print(test_prime(7))


# ...........question ....10).print the even numbers from a given list.

# def even_list():
#     a=[1,2,3,4,5,6,7,8,9]
#     b=[]
#     for i in a:
#         if i%2==0:
#             b.append(i)
#     print(b)
# even_list()


# ......question..11)..

# def perfect_number(n):
#     sum = 0
#     for x in range(1, n):
#         if n % x == 0:
#             sum += x
#     return sum == n
# print(perfect_number(6))
 

# ....................#12).palin drom num in function 

# def palidrom_num():
#     n=int(input("enter"))
#     f=n
#     sum=0
#     while n>0:
#         sum= (sum*10)+(n%10)
#         n=n//10
#     if f==sum:
#         print("true")
#     else:
#         print("false")

# palidrom_num()

# ...13)..........................paskal tringle 

# p=int(input("enter the number"))
# for i in range(1,p+1):
#     for j in range(0,p):
#         print("",end="")
#     c=1
#     for j in range (1,i+1):
#         print("",c,end=" ")
#         c=c*(i-j)//j
#     print()





