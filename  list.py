#       list....start.....
# list=["dilli","kolkatta","mummbai","bihar"]
# list.reverse()
# print(list)


# .............list......

# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# add=0
# for i in range (0,3):
#     for j in range (0,5):
#         x=(marks[i][j])
#         add+=x
# print(add)

# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78]]
# add=0
# for i in range (len(marks)):
#     for j in range (len(marks[i])):
#         x=(marks[i][j])
#         add+=x
# print(add)

# .......... all numbers add...!
# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78],[87, 67, 49, 68, 88]]
# add=0
# for i in range (len(marks)):
#     for j in range (len(marks[i])):
#         x=(marks[i][j])
#         add+=x
# print(add)


# tringle print 1 to 9.....
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print(i,end="")
#         j+=1
#     print()
#     i+=1

# ......practic question  .....try to chek...rajesh!
# n=9
# i=1
# for i in range (1,n):
#     if i!=7:
#         print(str(i)*i)
#     else:
#         print("raja  "*i)

# .............meraki question.............


# n=[10,11,12,13,14,17,18,19,20,10,11,9]
# n2=[]
# add=0
# for i in (n):
#     a=[]
#     for j in (n):
#         if i+j==30:
#             a.append(i)
#             a.append(j)
#     if len(a)>0:
#         n2.append(a)
# print(n2)

# ....... pair find = 30.........

# n=[10,11,12,13,14,17,18,19,20,10,11,9]
# n2=[]
# add=0
# for i in (n):
#     a=[]
#     for j in (n):
#         if i+j==30 and len(a)<2:
#             a.append(i)
#             a.append(j)
#     if len(a)>0:
#         n2.append(a)
# print(n2)


# .......pair find 30 ....
# a=[10,11,12,13,14,17,18,19]
# e=[]
# for b in a:
#     for c in a:
#         if b+c== 30:
#             e.append([b,c])
#             a.remove(b)
# print(e)

# ........last ka digit nikalkar pitche  add....!
# n=123456
# a=n%1000
# e=n//100
# f=n%100
# b=a//100
# g=f*10+b
# c=e*1000+g
# print(c)

# ..........list len function...in meraki...question................

# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]
# for a in range(5):
#     print(students[a],marks[a],end=" ")


# ......binary to decimal input leke..................!
# a = []
# b = int(input("enter the number: "))
# for i in range(b) :
#     x = int(input("enter any charecter or number:  "))
#     a.append(x)
# print(a)
# a.reverse()
# sum = 0
# for j in range(len(a)):
#     sum = 2 ** j * a[j] + sum
# print("your binary to decimal number is = ",sum)


# a = ["raja","aniket","bhumesh","akash","kumawat"]
# for i in range(-1,-(len(a)+1),-1) :
#     print(a[i])

# .....binary to decimal......!
# a = [1,0,0,1,1,0,1,1]
# sum = 0
# for j in range(-1,-(len(a)+1),-1) :
#     sum = 2 ** ((-(j))-1) * a[j] + sum
# print("your binary to decimal number is = ",sum)


# a = [1,0,0,1,1,0,1,1]
# add = 0
# for j in range(-1,-(len(a)+1),-1) :
# 	add = 2 ** ((-(j))-1) * a[j] + add
# print( " your binary to decimal is number =  ", add)

# .... list of sum and even = sum...
# a = [1,2,3,4,5,6,7,8,9,10]
# even = 0
# odd = 0
# for i in a :
#     if i % 2 == 0 :
#         even = even + i
#     else :
#         odd += i
# print("sum of even number is = ",even,"sum  of odd number is = ", odd,"sum of all numbers is",odd+even)

# .....palidrom tringle pattern print.......!
# for i in range (1,5):
#   print((10**i//9)**2)


# .....how to table print.....!

# i=1
# n= int(input("enter"))
# while i <=10:
#     print(f"{n}*{i}={n*i}")
#     i+=1


# .........mini kbc...........!

# a=["1).what is capital of india","2).he is my friend"]
# b=[["1).himachal","2).punjab","3).dillhi","4).hariyana"],["1).aniket","2).raja","3).bhumesh","4).akash"]]
# c=[3,4]
# for i in range (len(a)):
#     print(a[i])
#     for j in  (b[i]):
#         print(j)
#     n=int(input("enter"))
#     if c[i]==n:
#         print("you win")
#     else:
#         print("you loss")


# .#....how to count capital , smallest , and number given string....
# a=input("enter number")
# count=0
# count1=0
# count2=0
# for x in a:
#     if x.isupper():
#         count+=1
#     elif x.islower():
#         count1+=1
#     elif x.isnumeric():
#         count2+=1
# print(count)
# print(count1)
# print(count2)

# ..palidrom tringle print..
# for x in range (1,5):
#     for y in range (4,x,-1):
#         print(" ",end=" ")
#     for z in range(x-1,-x,-1):
#         print(x-abs(z),end=" ")
#     print()

# ....decimal to binary....
# n = int(input("enter the decimal number: "))
# a =[]
# while n != 0 :
#     b = n % 2
#     a.append(b)
#     n = n // 2
# a.reverse()
# print("your binary number is = ",a)


# ...binary to decimal.....!
# a=[1,0,0,1,1,0,1,1]
# a.reverse()
# length=len(a)
# add=0
# for i in range (0,length):
# 	add=2**i*a[i]+add
# print(add)


# list=[[8,3,4],
#       [1,5,9],
#       [6,7,2]]

# isMagic=True
# for i in range(len(list)):
#     raw_sam=0
#     colan_sam=0
#     d1=0
#     d2=0


#     d1+=list[i][i]
#     d2=list[i][len(list[0])-i-1]


#     for j in range(len(list[0])):
#         raw_sam+=list[i][j]
#         colan_sam+=list[j][i]

#     if raw_sam!=colan_sam and d1!=d2:
#         isMagic=False
#         break


#     if isMagic:
#         print("this is magic squre")
#     else:
#         print("this is not magic squre")


# ...debuging...... in list question.....
# marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
# total_marks = 0
# counter = 0
# while counter < len(marks):
#     total_marks = total_marks + int(marks[counter])
#     counter = counter + 1
# print(total_marks)
# print(counter)


# ...........debuging..... list( last question)
# name = ["Savitri", "Phule", "26"]
# Ab hum iss list ko use karke poora naam (full name) print karna chaste hai
# print(name[0])


# ......fully....kbc...kaun banega karorpati......@.....#


# import random
# a=[").what is capital of india",
# ").he is my friend",
# ").wich companey has shut down its smart phone business",
# ").who is father of nation of india",
# ").wich animal is called king of junggle",
# ").wich is the longest river in india",
# ").what is taught in navgurukul",
# ").national language of india",
# ").national fruit of india",
# ").national sweet of india",
# "(switch Qustion).what is my name "]

# b=[["1>.himachal","2>.punjab","3>.dillhi","4>.hariyana","5>.life-line"],
# ["1>.aniket","2>.raja","3>.bhumesh","4>.akash","5>.life-line"],
# ["1>.vivo","2>.lg","3>.oppo","4>.sumsung","5>.life-line"],
# ["1>.gandhi","2>.nehru","3>.bhim","4>.kabir","5>.life-line"],
# ["1>.lion","2>.rabbit","3>.tiger","4>.cammal","5>.life-line"],
# ["1>.ganga","2>.nil","3>.satlaj","4>.bhagirathi","5>.life-line"],
# ["1>.python","2>.coding","3>.manejment","4>.html","5>.life-line"],["1>.english","2>.hindi","3>.urdu","4>.tamil","5>.life-line"],
# ["1>.mango","2>.littchi","3>.banana","4>.guava","5>.life-line"],
# ["1>.rasgulle","2>.peda","3>jalebi","4>laddu","5>.life-line"],
# ["1>.Praveen","2>.raja","3>.aniket","4>.bhumesh"]]

# c=[3,4,2,1,1,1,2,2,1,3,2]
# life=["1).50-50","2).phone of friend","3).audiance poll","4).switch question"]

# life1=[["3>.delhi","1>.himachal"],["3>.bhumesh","4>.akash"],["2>.lg","3>.oppo"],
# ["1>.gandhi","2>.nehru"],["1>.lion","2>.rabbit"],
# ["1>.ganga","3>.satlaj"],["2>.coding","3>.manejment"],["2>.hindi","3>.urdu"],["1>.mango","4>.guava"],
# ["3>jalebi","4>laddu"]]
# d=50000
# l1=0
# l2=0
# l3=0
# l4=0
# m=1
# while m>0:
#     m2=random.randint(1,101)
#     m3=random.randint(1,101)
#     m4=random.randint(1,101)
#     m5=random.randint(1,101)
#     if m2+m3+m4+m5==100:
#         break
#     else:1
#     m=m+1
# lis=[0,1,2,3,4,5,6,7,8,9]

# for i1 in range (len(a)):
#     d=d*2
#     print('\033[37m',"*).this question for amount=",d,'\033[0m')
#     i=random.choice(lis)
#     print('\033[33m',str(i1+1)+a[i],'\033[0m')
#     print()
#     lis.remove(i)
#     for j in  (b[i]):
#         print(j)
#     print('\033[41m',"chose_option :-enter",'\033[0m')
#     n=int(input())
#     if n==5:
#         if l1==1:
#             print('\033[42m',"allready used by-50-50",'\033[0m')
#         if l2==1:
#             print('\033[42m',"allready used by phone a friend",'\033[0m')
#         if l3==1:
#             print('\033[42m',"allready used by audiance-poll",'\033[0m')
#         if l4==1:
#             print('\033[42m',"allready used by switch question",'\033[0m')
#         for a1 in (life):
#             print('\033[28m',a1,'\033[0m')
#         l=int(input("enter your choice: "))
#         #..50-50_life_line
#         if l==1 and l1<1:
#             for j in life1[i]:
#                 print(j)
#             v = int(input("enter your answer: "))
#             l1+=1
#             life.remove("1).50-50")
#             n=v
#         #..phone of friend..
#         elif l == 2 and l2<1:
#             print('\033[45m','Your friend suggest',c[i],'\033[0m')
#             v=int(input('enter your answer'))
#             l2+=1
#             life.remove("2).phone of friend")
#             n=v
#             print()
#         #audiance poll
#         elif l==3 and l3<1:
#             print('\033[39m',str(m2)+'% audiance want option 1>','\033[0m')
#             print('\033[39m',str(m3)+'% audiance want option 2>','\033[0m')
#             print('\033[39m',str(m4)+'% audiance want option 3>','\033[0m')
#             print('\033[39m',str(m5)+'% audiance want option 4>','\033[0m')
#             v=int(input('enter your answear'))
#             l3+=1
#             life.remove("3).audiance poll")
#             n=v
#             print()
#         #..switch-question..
#         elif l==4 and l4<1:
#             i=10
#             print(a[i])
#             print()
#             for j in  (b[i]):
#                 print(j)
#             print("chose_option :-enter")
#             l4+=1
#             life.remove("4).switch question")
#             n=int(input())

#     if c[i]==n:
#         print("congratulations. you_win . your answer is right",d)

#         print()
#     else:

#         print()
#         n=input("you want to game continue yes or no :-")
#         if n=="yes":
#             continue

#         else:
#             break

# #...how to list ke undar loop run....

# list=[i for i in range(1,151)]
# print(list)


# how to multipal list open....#
# n=[1,2,3,[4,5,6,[7,8,9]]]
# t=[]
# for i in len(n):
#     if type(i)==list:
#         n.remove(i)
#         print(n)

# ......table...............print..........#


# i=1
# n= int(input("enter"))
# while i <=10:
#     print(f"{n}*{i}={n*i}")
#     i+=1


# delly 2 question list, loop, if else
# dally .date copy me


# data = [1, [2, 3, [4, 5]], 6, [[7], [8, 9]]]
# flat_list = []

# # function
# def flatten_list(data):
#     # iterating over the data
#     for element in data:
#         # checking for list
#         if type(element) == list:
#             # calling the same function with current element as new argument
#             flatten_list(element)
#         else:
#             flat_list.append(element)

#


# print (second largest number [-2].......#

# without sort use...........
# a=[12,434,54,65,76]

# for i in range (0,len(a)):
#     for j in range (i+1,len(a)):
#         if a[i] > a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)
# print(a[-2])


# n=..... gussing game......#


# import random
# a=[3,2,5,6,7,4]
# for i in range(len(a)):
#     n=int(input("guss the number"))
#     h = random.choice(a)
#     if n==h:
#         print("congratulation :-you win")
#         break
#     else:
#         print("you loss")
#         print("plz try agin")


# ............extra Question.........#............in-list.......#


# ..1).Question
# a=[23,54,3,4,5,6]
# sum=0
# for i in a:
#     sum+=i
# print(sum)

# 2).
# a=[3,2,4,8,]
# m=1
# for i in a:
#     m=m*i
# print(m)


# jp question...............list.........dictionary most_important question .......

# t=['2', '3', '4', '5', '6', 'i', 'o', 'i', 'u', 'y', 't', 'r', 'e', 'k', 'j', 'h', 'g', 'f', 'e', 'w', 't', 'y', 'j', 'h', 'g', 'f', 'd',
#  's', 'a', 'h', 't', 'r', 'e', 'w', 'u', 'y', 't', 'r']
# a=[]
# count=0
# for  i in t:
#     for j in t:
#         if i==j:
#             count+=1
#     a.append([i,count])
#     count=0
# print(a)


# ..jp question.............

# L=[1,5,10,12,16,20]
# M=[1,2,10,13,16]
# n=[]
# p=[]
# for i in (L,M):
#     if n not in i:
#         n.extend(i)
# for j in n:
#     if j not in p:
#         p.append(j)
# print(sorted(p))


# flatein list in function....

# l = [1, 2, [3, 4, [5, [[[6]], 7], 8, [9, [10,[12,45,34]]]]]]
# output = []
# def call(l):
#     for i in l:
#         if type(i) == list:
#             call(i)
#         else:
#             output.append(i)

# print ('The original list: ', l)
# call(l)
# print ('The list after removing nesting: ', output)


# extra.question.mahendra....#......................extra.question......>

# a=[1,3,5,6,4,7,9,10]
# b=int(input("enter the number:"))
# for i in a:
#     if i==b:
#         x=a.index(b)
#         a[x]=[b]
# print(a)

# ...........................>
#     if 5 ==i:
#         b.append([i])
#     else:
#         b.append(i)
# print(b)


# a="apple"
# x=("-".join(a))
# y=x.split("-")
# print(x)
# print(y)


# extra.Question......list

# Q.find out diffrent between two list..1)

# l1=[1,2,3,8]
# l2=[2,3,4,0,6,9]
# l3=[]
# l4=[]
# for j in l1:
#     if j not in l2:
#         l3.append(j)
# print(l3)
# for i in l2:
#     if i not in l1:
#         l4.append(i)
# print(l4)


# remove all the unice value from a list:..2).

# a=[1,2,3,3,5,1,4,8,9]
# b=[]

# for i in a:
#     if a.count(i)>1:
#         if i not in b:

#             b.append(i)
# print(b)

# ......3).

# sort ka use hum list me karte ha or list modifay
# ka sorterd ka use hum dictionary me karte ha or list dono me  sec


# ..4).bubble sort..
# a=[1,2,3,6,8,5,9,56,33,75]
# b=[]
# for i in range (a):


# ..5).


# a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print("which value remove in list plz")
# while True:
#     b=int(input("enter:"))
#     if b<=len(a):
#         for i in a:
#             if i==b:
#                 x=a.index(i)
#                 a.remove(b)

#         print(a,"[index of (a)]=",x)
#     else:
#         print("'sorry'list out of range")


# n=..... gussing game......#


