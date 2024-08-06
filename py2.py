def p1():
    a=input("what's your name:")
    print("Hello!!!")
p1()

def p2():
    a=int(input("Enter first number:"))
    b=int(input("Enter second No.:"))
    print("the total sum is :",a+b)
p2()


def p3():
    principal=int(input("enter principal:"))
    rate=int(input("enter rate:"))
    time=int(input("enter time:"))
    print(f"the simple interest is:",principal*rate*time/100)
p3()

def p4():
    a=int(input("Enter first number:"))
    b=int(input("Enter second No.:"))
    c=a
    a=b
    b=c
    print("after switching",a,b)

p4()    

def p4():
    a=int(input("Enter first number:"))
    b=int(input("Enter second No.:"))
    a=a+b
    b=a-b
    a=a-b
    print(a,b)
p4()   


def p5():
    a=int(input("Enter first number:"))
    b=int(input("Enter second No.:"))
    r=int(input("enter the rudias:"))
    areaofcir=3.14*r*r
    arearofrec=a*b
    print("area of circle",areaofcir)
    print("area of rectangle",arearofrec)

p5()    




def p6():
    a=int(input("Enter first number:"))
    # b=int(input("Enter second No.:"))
    if(a/2==0):
        print('even number')

    else:
        print("ohh! it's a odd no.")

p6()        

def p7():
    a=int(input("Enter first number:"))
    b=int(input("Enter second No.:"))
    c=int(input("Enter third no."))
    if(a>b and a>c ):
        print("A IS BIG")
    elif(b>a and b>c):
        print("B IS BIG")
    else:
        print("C IS BIG")

p7()                

def p8():
    a=int(input("Enter first number:"))
    # b=int(input("Enter second No.:"))
    if(a%400==0 and a%100==0):
        print("the year is a leap year")
    elif(a%4==0 and a%100!=0):
        print("the year is a leap year")
    else:
        print("the no. is not a leap year") 

p8()               


def p9():
    suba=int(input("Enter first sub:"))
    subb=int(input("Enter second sub:"))
    subc=int(input("enter third sub"))
    average=(suba+subb+subc)/3
    if(average<=100 and average>=90):
        print("Grade is a")
    elif(average<=89 and average>=80):
        print("Grade is b")
    elif(average<=79 and average>=70):
        print("Grade is c")
    elif(average<=78 and average>=60):
        print("grade is d") 
    elif(average<=59 and average>=0):
        print("Grade is F")               

p9()

def p10():
       a=input("Enter first number:")
       if(a=="a" or a=="u" or a=="e" or a=="i" or a=="o"):
           print("it's is vovel")
       else:
           print("it's consonent") 


p10()              


def p11():
    for i in range(0,11):
       if i==5:
         continue
       print(i)
       

p11()     

def p12():
    s=0
    i=2 
    while(i<=20):
        s=s+i
        i+=1
    print(s)      
p12()

def p13():
    a=10
    b=2
    print(a**b)
p13()

def p14():
    a=int(input("enter number you want to reverse:"))   
    reverse =0
    while(a>0):
        digit=a%10
        reverse=reverse*10+digit
        a//=10
    print(reverse)
p14()    
a=int(input("Enter first number:"))
def p15(a):
    
     if(a>=1):
         p15(a//2)
         print(a%2,end="")




def p16():
    for i in range(5):
      print(end=" ")
      print("\n")
      for j in range(i):
        # print(end="")
        print("*",end="")

    for g in range(1,6):
        print(end="")
        print("\n")
        for k in range(g):
            print(g,end="")


# print(end="")        


p16()        


import math
def p17():
    a=25
    b=lambda a:math.sqrt(a)
    print(b(a))

p17()

def p18():
    a=[1,2,3,4,5,6]
    a.insert(7,7)
    print(a)
    a.remove(3)
    print(a)
    a.append(3)
    print(a)
    len(a)
    print(len(a))
    a.pop()

    print(a)
    a.clear()
    print(a)

p18()    

def p19():
    a={1:1,2:3,4:5,6:7}
    print(a)
    print(a.items())  
    a[1]=2
    print(len(a))  
    print(a)
p19()


def p20():
    a=(1,2,3,4,5)
    b=(6,)
    a+=b
    print(a)


p20()


def p21():
    a={1,2,3,4,5}
    a.add(6)
    b={0}
    b.update(a)
    print(b)
    x=a.copy()
    print(x)
    a.pop()
    print(a)
    print(a.remove(3))
    print(a.discard(2))
    print(x.clear())
    print(a.union(b))
    print(a.intersection(b))
    print(a.difference(b))



p21()

def p22():
    x="malayalam"
    y=x[::-1]
    if x==y:
        print(" polidrome")
    else:
        print("not poplidrome")
    print(x) 

p22()

def p23(a):
    if a==1:
        return 1
    else:
        return a*p23(a-1)

res=p23(5)
print(res)    


def p24():
    import csv
    with open("dv.csv","r") as file:
        reader =csv.reader(file)
        for row in reader:
            print(row)
p24()            

def p25():
    import csv 
    people =[{
        "p":"nice"

    }]

    field=['p']
    filename="dv.csv"
    with open(filename,"w") as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=field)
        writer.writeheader()
        writer.writerows(people)

p25()        


def p26():
    import numpy as np
    a=np.matrix([[1,2,3],[2,3,5],[47,5,3]])
    b=np.matrix([[1,2,3],[2,3,5],[7,5,3]])
    print(a)
    result=np.add(a,b)
    print(result)

p26()



def p27():
    class parent:
        def go(self):
            print("hi from parent")

    class child(parent):
        def sum(self):
            print("hi from child") 

    obj=child()
    obj.go()
    obj.sum()              

p27()


def p28():
    try:
        k=5/0
        print(k)
    except ZeroDivisionError:
        print("can't divide by zero")

p28()            
    



    