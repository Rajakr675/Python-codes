
# ..important task mix python Question:



#  same key add values......
# d1={1:10, 2:20}
# d2={3:30,2:40}
# d3={5:50,1:60}
# e={}
# for d in d1,d2,d3:
#     for k in d.keys():
#         e[k]=e.get(k,0)+d[k]
# print(e)


# list1=['one','two','three','four','five']

# list2=[1,2,3,4,5,]
# l3=dict(zip(list1,list2))
# print(l3)




# employs ..question..very imporatant task..list or dictionary.....mahendr .


# a=['employee1','employee2','employee3']
# b=['raja','akash','bhumesh']
# c=['sex_male','sex_male','sex_male']
# d=[21,24,23]
# e=[['post_HR',50000,3],['post_pioun',60000,5],['post_cleark',70000,7]]
# f={}
# # f={a[i]:{'name':b[i],'sex':c[i],'age':d[i],'other-detels':{"post":e[i][0],"salary":e[i][1],"year":e[i][2]}} for i in  range (len(a))}
# for i in range (len(a)):
#     f.update({a[i]:{'name':b[i],'sex':c[i],'age':d[i],'other-detels':{"post":e[i][0]},"salary":e[i][1],"year":e[i][2]}})
# print(f)

# ..........................flatin list i function 
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


# list ko splite kaise kare seprate se!  try and chek...............................question..............................#
# 1st..type..normal....

# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# n=int(input("enter"))
# b=[]
# for y in range ((len(a)+n-1)//n):
#     x=a[n*y:n*(y+1)]
#     b.append(x)y
# print(b)


# 2ed..type..from function..


# def split_list(n):
    
#     a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
#     b=[]
#     for y in range ((len(a)+n-1)//n):
#         x=a[n*y:n*(y+1)]
#         b.append(x)
#     print(b)
# n=int(input("enter"))
# split_list(n)

# ..3rd..type.list_comprihantion

# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# n=int(input("enter"))
# b=[a[n*y:n*(y+1)] for y in range((len(a)+n-1)//n)]
# print(b)


