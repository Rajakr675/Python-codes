# dictonery.....meraki question

# ..1.type

# d1={1:10, 2:20}
# d2={3:30,2:40}
# d3={5:50,1:60}
# e={}
# for d in d1,d2,d3:
#     for k in d.keys():
#         e[k]=e.get(k,0)+d[k]
#         print(e)



# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

# Example
# dict= {"brand": "Ford","model": "Mustang","year": 1964}
# dict["color"] = "red"
# print(dict)


#....... methods

# # Add a color item to the( dictionary by using )the update() method:

# thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
# thisdict.update({"color": "red"})
# print(thisdict)


# The pop() method removes the item with the specified key name:

# thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
# thisdict.pop("modal")
# print(thisdict)

# ..1.type.......start..

# d1={1:10, 2:20}
# d2={3:30,2:40}
# d3={5:50,6:60}
# d={}
# for i in d1,d2,d3:
#     d.update(i)
# print(d)



#....2.Question.........

# dict={"name":"raju","marks":"56"}
# print(dict)
# n=input("etr you")
# if n in dict:
#     print("h")
# else:
#     print("n")



#....3).Question.......all item ko sum kaise kare......#

# my_dict = {'data1':100,'data2': -54,'data3': 247}
# sum=0
# for i in my_dict:
#     sum+=(my_dict[i])
# print(sum)


# type ...2

# my_dict = {'data1':100,'data2': -54,'data3': 247}
# Values=my_dict.values()
# total=sum(Values)
# print(total)


#.. saare item ko bahar kaise print kare...#
# my_dict = {'data1':100,'data2': -54,'data3': 247}
# for a in (my_dict.items()):
#     print(a)




#.. saare (values) ko bahar kaise print kare...#
# my_dict = {'data1':100,'data2': -54,'data3': 247}
# for a in (my_dict.values()):
#     print(a)
    



#..4).Question.......nested dict me jaa ke iteam delet kaise kare ..#

# dic= {1:'navgurukul',
#         2:'in', 
#         3:{'A' : 'WELCOME',
#            'B' : 'To',
#            'C' : 'DHARAMSALA'
#           }
#           }
# del dic[3]['A']
# print(dic)


#....5).Question.....#how to convert list into dictonery.with keys values..#

# list1=['one','two','three','four','five']
# list2=[1,2,3,4,5,]
# k=dict(zip(list1,list2))
# print(k)

#..6).Question....#
# dic={'ball':'red','bat':4,'wickets':8,'ball'green,'bat':3}














#..7)..






#..8).Question......Take input of name and marks of 10 students and store to a dictionary.
# list1=[]
# list2=[]
# for i in range (1,4):
#     a=input("enter-name")
#     b=int(input("enter-marks"))
#     list1.append(a)
#     list2.append(b)
#     k=dict(zip(list1,list2))
# print(k)

#..9)...













#..10)...Question.......Count the total number of items from the values of the dictionary which are in the form of a list.


# dict1 =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# c=[]
# for j in dict1.values():
#     if type(j) ==list:
#         c.extend(j)
# print(len(c))


#..11)..Question..3 highest values of a given dictionar

# my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# c=[]
# for i in my_dict.values():
#     c.append(i)
# c.sort()
# print(c[3:])




# ..12)..Question..1.type.. 

#...1)..type....
# a={a:a**2 for a in range(1,15)}
# print(a)

#..2..type....

# list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# list2=[1,4,9,16,25,36,49,64,81,100,121,144,169,196,225]
# a=dict(zip(list1,list2))
# print(a)


# ..type 3.....
# p = {}
# b=int(input("enter"))
# for i in range (1,b):
#     c=i*i
#     p[i]=c
# print(p)
    

#..13)..Question
# my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# c=[]
# for i in my_dict.keys():
#     c.append(i)
# c.sort()
# print(c[-3:])

# #..14).Question.





#.. w3 resurace.....................................................#...w3 resurace...........................#

#..1).question........

# # import operator
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print('Original dictionary : ',d)
# sorted_d = sorted(d.items(), key=operator.itemgetter(1))
# print('Dictionary in ascending order by value : ',sorted_d)
# sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
# print('Dictionary in descending order by value : ',sorted_d)


#..2).question.........

# d={0: 10, 1: 20}
# d.update({2:30})
# print(d)

#..3).question........multipal dictonery how can add.

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# for i in (dic1,dic2,dic3):
#     dic4.update(i)
# print(dic4)

#..4).question......









# #..5).question.....
# d={'x':10 , 'y':20 ,'z' :30}
# for k,v in d.items():
#     print(k,'->',v)


#..6).question..

# print({a:a**2 for a in range(1,6)})


#..7)..question.....
# a={a:a**2 for a in range(1,16)}
# print(a)




# #..8).question.....
# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# d= d1.copy()
# d.update(d2)
# print(d)

#..2 type ....


# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# d3={}
# for k,v in (d1.items(),d2.items()):
#     d3.update({k,v})
# print(d3)

#..10).question...Write a Python program to (sum all) the items in a dictionary. 

# dict= {'data1':100,'data2':-54,'data3':247}
# b=(sum(dict.values()))
# print(b)

#..11).question Write a Python program to (multiply all) the items in a dictionary.

# dict={'a':5, 'b':4 ,'c':3}
# multi=1
# for i in dict:
#     multi=multi* dict[i]
# print(multi)

#..12).question...write a Python program to remove a key from a dictionary.

# myDict = {'a':1,'b':2,'c':3,'d':4}
# print('original_dict',myDict)
# del myDict['a']
# print(myDict)

#..13).question....Write a Python program to map two lists into a dictionary. 

# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# dict = dict(zip(keys,values))
# print(dict)


# ..14).question....Write a Python program to sort a given dictionary by key.














#..15)......Write a Python program to get the maximum and minimum value in a dictionary.

# my_dict = {'x':500, 'y':5874, 'z': 560}
# b=[]
# for i in my_dict.values():
#     b.append(i)

# print(max(b))
# print(min(b))

# ..16).question....Write a Python program to get a dictionary from an object's fields.

# d1=['x','y','z']
# d2=['red','yellow','green']
# b=dict(zip(d1,d2))
# print(b)


# ..17).question..... Write a Python program to remove duplicates from Dictionary.







#..18).question..Write a Python program to check a dictionary is empty or not.
# my_dict = {}

# if len(my_dict) == 0:
#     print("Dictionary is empty")
    


# ..19).questiom,,,,Write a Python program to combine two dictionary adding values for common keys.
# import Counter
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3={}
# for x,y in d1,d2:
#     if x==y:
#         d=d1.values()+d2.values()
#         d3.update({x:d})
#     else:
#         d3.update({x:d1.values()})
#         d3.update(({y:d2.values()}))
# print(d3)



# ..20).question..
# l = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# m=[]
# n=[]
# for i in l:
#     for j in i.values():
#         n.append(j)
# for b in n:
#     if b not in m:
#         m.append(b)
# print(set(m))

# ..21quetion.









# ..22.QUESTION..Write a Python program to find the highest 3 values of corresponding keys in a dictionary.


# m = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# list=[]
# b=sorted(m.items(),key=lambda t:t [1])
# a=(b[3:])
# d1=dict(a)
# for f in (d1.keys()):
#     list.append(f)
# print(list)

# ..23question......


# l= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# for k,v in itemes():

 








# .24...........

# str1= 'w3resource'
# m = {}
# count=0
# for i in str1:
#     for j in str1:
#         if i==j:
#             count+=1
    
#     m.update({i:count})
#     count=0
# print(m)
        
  


# ..25).Question.................

 










#  crud opration on dictonary.............C.R.U.D........OPRATION...................................


# a={}
# while True:
#     print("""
#      press 1 for creat
#      press 2 for read
#      press 3 for update
#      press 4 for delete
#      press 5 for exit
#           """)
#     b=int(input("enter the choice:"))
#     # creat
#     if b==1:
#         c=int(input("enter the mo.number:"))
#         a[c]=[input("enter your name: "),input("enter your email: "),input("enter your address: ")]
#         print(a)
#     # read
#     elif b==2:
#         print("[wich mobile number want to read]")
#         d = int(input("enter your ragister mo.number:- "))
#         if d in a:               
#             print(a[d])
#         else:
#             print("your enter number is wrong\nplease try again")
#     # update
#     elif b == 3:
#         print("wich mobile nuber id want to update ")
#         e = int(input('enter the ragister mo.number: '))
#         if e in a:
#             f=[input("enter your name: "),input("enter your email: "),input("enter your address: ")]
#             a[e]=f
#             print(f)
#         else:
#             print('not exist')
#     # delete
#     elif b ==4:
#         m=int(input("wich mo.number  you want to delete:"))
#         if m in a:
#             a.pop(m)
#         else:
#             print("number not found")
#         print(a)
#     # exist
#     else:
#         break
    

# .dict question badhiya question.....akash.....
# ....1st type

# a=[[1,'akash','v'],[2,'bhumesh','raja'],[3,'raja','3']]
# d = {}
# for j in a:
#     if j[0] not in d.keys():
#         d.update({j[0]:[j[1],j[2]]})
# print(d)
 
#  2ed type...sort only two lines

# a=[[1,'akash','v'],[2,'bhumesh','raja'],[3,'raja','3']]
# print({j[0]:[j[1],j[2]] for j in a})


# how to count value

# a=int(input("enter"))
# c=0
# while a>0:
#     y=a%10
#     c+=1
#     a=a//10
# print(c)

#  30) question

# data = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# data=sorted(data.items(),key =lambda items: items[1],reverse=True)
# print(data[:3])


# ..31)..question

# d= {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print("key value count")
# count=0
# for i,j in d.items():
#     count+=1
#     print(i," " ,  j ," ",    count)

# ..32)..qustion....

# students = {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
# for a in students:
#     print(a)
#     for b in students[a]:
#         print (b,':',students[a][b])
		

# ..33)Question.....

# 


# ..34).question...
# dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# c=0
# for i in dict.values():
#     for j in i:
#         c+=1
# print(c)


# ..35).question..

# data={'Math':81, 'Physics':83, 'Chemistry':87}
# list1=sorted(data.items())



# ...36).question.......
# 1st type

# list1= ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# list2 = [1, 2, 2, 3]
# dict1={}
# for i,j in zip(list1,list2):
#     dict1.update({i:{j}})
# print(dict1)
    
# 2ed type...without zip function......................
# list1= ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# list2 = [1, 2, 2, 3]
# c={ }
# for i in range (len(list1)):
#     c[list1[i]]={list2[i]}
# print(c)


# ..38)..QUESTION.........

# x = {'key1': 1, 'key2': 3, 'key3': 2}
# y = {'key1': 1, 'key2': 2}
# c={}
# for i,j in x.items():
#     for n,m in y.items():
#         if 
# ..39)....question..





# ..40)..jsun question




# ..41).quetion

# 1st..type

# dict1 = {'c1': 'Red','c4':None, 'c2': 'Green', 'c3':None}
# d={x:y for x,y in dict1.items() if y!=None}
# print(d)

# 2ed.type..none value remove 

# dict1 = {'c1': 'Red','c4':None, 'c2': 'Green', 'c3':None}
# d={}
# for x,y in dict1.items():
#     if y==None:
#         continue
#     d.update({x:y})
# print(d)



# ..42)..Question......

# marks = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# print("Original Dictionary:")
# print(marks)
# print("Marks greater than 170:")
# m={k:v for k,v in marks.items() if v>=170}
# print(m)


# ..43)..question......

# a=['S001', 'S002', 'S003', 'S004']
# b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# c=[85, 98, 89, 92]
# for i,j,k in zip(a,b,c):
#     print({i:{j:k}},end="")
  

# ..44)question...
 
# students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 65), 'Pierre Cox': (5.8, 66)}
# print("Original Dictionary:")
# print(students)
# for k,v in students.items():
#     if v[0] >=6.0 and v[1] >=70:
#         print(k,v)

# ..46)...question.....

# d= [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# a={}
# for i,j in d:
#     a.setdefault(i, []).append(j)
# print(a)


# ..47).question

# m= {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# l1=[y for y in m.keys()]
# l2=[y for y in m.values()]
# # print(l1)
# # print(l2)
# a=[]
# b={}

# for i in range(len(l2[0])):
#     b=((l1[0],l2[0][i]),(l1[1],l2[1][i]))
#     a.append(dict(b))
# print(a)

# ..49..question.........

# d=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# a,b = d
# n = {}
# m = {}
# c = []
# for t,y in a.items():
#     g = {t:int(y)}
#     n.update(g)
# for k,v in b.items():
#     h = {k:int(v)}
#     m.update(h)
#     rt = n,m
# for o in rt:
#     c.append(o)
# print(c)


# # .............................................adhura ha  puhana ha 

# # ..50..)question...

# d= { 
#     'C1' : [10,20,30], 
#     'C2' : [20,30,40],
#     'C3' : [12,34]
#     }
# for i in d:
#     d[i].clear()
# print(d)

# ..51..question...
# d= { 
#                'Math' : [88, 89, 90], 
#                'Physics' : [92, 94, 89],
#                'Chemistry' : [90, 87, 93]
#              }
# print(d)
# d['Math'] = [x+1 for x in d['Math']]
# d['Physics'] = [x-2 for x in d['Physics']]

# print(d)

# ..52).question..

# marks = [{'Math': 90, 'Science': 92}, 
#          {'Math': 89, 'Science': 94}, 
#          {'Math': 92, 'Science': 88}]
# t=[]
# for j in marks:
#     t.append(j['Math'])
# print(t)


# ..53)..question..find the length of a given dictionary values.

# d= {1 : 'red', 2 : 'green', 3 : 'black', 4 : 'white', 5 : 'black'}
# l= {value: len(value) for  value in d.values()}
# print(l)

# ..55)..question....
# 1st type 
# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# for k in num.keys():
#     print(k)

# 2ed type
# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# print(list(num)[0])
# print(list(num)[1])
# print(list(num)[2])

# 3rd type
# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# print(list(num))



# ..56..question.....

# dic= {1 : 'red', 2 : 'green', 3 : 'black', 4 : 'white', 5 : 'black'}
# l=[]
# for k,v in dic.items():
#     l.append([k,v])
# print(l)

# ..57..question.


# d= {'V' : [1, 4, 6, 10], 'VI' : [1, 4, 12], 'VII' : [1, 3, 8]} 
# c={}
# for k,v in d.items():
#     # print(v)
#     b=[]
#     for i in v:
#         if i%2==0:
#             b.append(i)
#     c.update({k:b})
# print(c)
    

# ..58)..question...





# ..59..question...
# d = {'a':5, 'b':14, 'c': 32, 'd':35, 'e':24, 'f': 100, 'g':57, 'h':8, 'i': 100}
# for k,v in d.items():
#     sorted(k)
# print(k)

# # audhura question


# 60...) question
# d={'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
# f=1
# g=[]
# for k,v in d.items():
#     if len(v)==f:
#         g.append(k)
# print(g)

# ..61.)question.............count the dictionary in value.


# d={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# count=0
# a={}
# for i in d.values():
#     for y in d.values():
#         if i==y:
#             count+=1
#     a.update({i:count})
#     count=0
# print(a)
    

# ..63)question...



# d=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'],
#   [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'],
#   [5, 'Zachary Simon', 'VII']]
# c={d[i][0]:[d[i][1],d[i][2]] for i in range (len(d))}
# print(c)

        
# # ..64)..question..
# d={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# 






# ..65)question.......count of all values in dict..

# d = {'#FF0000':'Red', '#800000':'Maroon', '#FFFF00':'Yellow', '#808000':'Olive'}
# count=0
# for i in  d.values():
#     for j in range (len(i)):
#         count+=1
# print(count)

# ..66question...





# 67..question....
# s= {'Ora Mckinney': 8,'Theodore Hollandl': 7,'Mae Fleming': 7,'Mathew Gilbert': 8,'Ivan Little': 7,}
# d={(value,key)for key,value in s.items() }
# print(d)
# ..........................adhura ha 

# ..68)..question
# d1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
# d2 = {'x': 300, 'y': 'Red', 'z': 600}
# for k,v in d1.items():
#     for i,j in d2:
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,adhura ha 



# ..69)..quewstion..........function question...........








# ...70)..question........






# ..72..question..

# s= {
#   'Theodore': 10,
#   'Mathew': 11,
#   'Roxanne': 9,
# }
# d={(value,key)for key,value in s.items() }
# print(d)

# ..73)..question.....kisis se puch sakte ho question

# d=[{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]

# for i in d:
#     print(i['age'])


# ..74)..question..

# u= {
#   'Theodore': { 'user': 'Theodore', 'age': 45 },
#   'Roxanne': { 'user': 'Roxanne', 'age': 15 },
#   'Mathew': { 'user': 'Mathew', 'age': 21 },
# }
# k=[]
# p=[]
# for i,j in u.items():
#     k.append(i)
#     p.append(j['age'])
#     g=dict(zip(k,p))
# print(g)
    

# ..75..question..

# s = {
#   'Theodore': 19,
#   'Roxanne': 20,
#   'Mathew': 21,
#   'Betty': 20
# }
# l=[]
# for k,v in s.items():
#     if v==20:
#         l.append(k)
# print(l)

# ..76 question...

# d=['a', 'b', 'c', 'd', 'e', 'f']
# e=[1, 2, 3, 4, 5]
# f=dict(zip(d,e))
# print(f)

# ..77).question..
# d={'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# f=tuple(d.items())
# print(list(f))

# 78..)question..

# d={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# f=[]
# for k in d.keys():
#     f.append(k)
# print(f)

# 79)..question..

# d={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# f=[]
# for v in d.values():
#     f.append(v)
# print(f)

# ...80 .)Question......last question

# d={'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# v = list(d.values())
 
# # taking list of car keys in v
# k = list(d.keys())
 
# print(k[v.index(max(v))])
# print(k[v.index(min(v))])



# without zip add two list in convert dictionary

# a=[5,7,8,9]
# b=[8,7,12,3]
# c={a[i]:b[i] for i in range(len(a))}
# print(c)



# .......................
