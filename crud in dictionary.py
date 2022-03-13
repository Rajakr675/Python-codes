#  crud opration on dictonary.............C.R.U.D........OPRATION...................................


a={}
while True:
    print("""
    press 1 for creat
    press 2 for read
    press 3 for update
    press 4 for delete
    press 5 for exit
          """)
    b=int(input("enter the choice:"))
    # creat
    if b==1:
        c=input("enter the mo.number:")
        if len(c)==10:
            a[c]=[input("enter your name: "),input("enter your email: "),input("enter your address: ")]
        
        else:
            print("please enter correct mobile number")
    # read
    elif b==2:
        print("[wich mobile number want to read]")
        d = (input("enter your ragister mo.number:- "))
        if d in a:               
            print(a[d])
        else:
            print("your enter number is wrong\nplease try again")
    # update
    elif b == 3:
        print("wich mobile nuber id want to update ")
        e = (input('enter the ragister mo.number: '))
        if e in a:
            f=[input("enter your name: "),input("enter your email: "),input("enter your address: ")]
            a[e]=f
            print(f)
        else:
            print('not exist')
    # delete
    elif b ==4:
        m=(input("wich mo.number  you want to delete:"))
        if m in a:
            a.pop(m)
        else:
            print("number not found")
        print(a)
    # exist
    else:
        break
    
    
