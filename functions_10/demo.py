#now we go with functions function we use for code reusability and divide complex task to smaller pieces and make sense in readability
a=10
b=20
print(a+b)
print(a-b)
print(a/b)
a=5
b=10
def arithmetic():    #fun defination
    print(a+b)
    print(a-b)
    print(a/b)
arithmetic()        #fun call
a=100
b=200
arithmetic()
#then functions with parameters then it called as positional arguments
def arithmetic(a,b):
    print(a+b)
    print(a-b)
    print(a/b)
arithmetic(10,200)
#brief about positional arguments
def login(username,password):
    if username=="ravi"and password=="6662":
         print("login successful")
    else:
        print("invalid input")
login("ravi","6662")#exact order
login("6662","ravi")#un order
#default arguments
def emp_info(name,email,address,pincode="502103"):
    print(f"emp name is {name} email is {email} and address is {address} address pincode is {pincode}")
emp_info("santosh", "santhoshreddya5553@gmail.com","plrp","9666") #argument overriden by parameter given in def
emp_info("santosh", "santhoshreddya5553@gmail.com","plrp") #we not passing argument it takes default
# keyword argument
def stu_info(name,score,cgpa,college,branch="csm"):
    print(f"student name is {name} his score is {score} and cgpa is {cgpa} and college is {college} his branch is {branch}")
stu_info(college="vasavi vce",name="santhoshreddy",cgpa="9.0cgpa",branch="cse",score="936")
#adding all arguments arbitrary positional arguments it takes like tuples
def adding(*all):
    total=0
    for i in all:
        total=total+i
    print(f"total is {total}")
adding(1,2,3,4)
#arbitrary keyword arguments it takes like dictionary
def empinfo(**proff):
    print(proff)
empinfo(name="santhosh",age="21",job="poultry business")  
#transaction histry  
def paytm(**info):
    print(info)
    total=0
    for i in info:
        total=total+info[i]
    print(f"ur total payments is {len(info)} and total is {total}")
    
paytm(mon=1000,tue=2000,wed=3000)
#combination of both * and **
def newpayment(*payments,**info):
    print(payments)
    print(info)
    total=0
    for i in payments:
        total=total+i
    print(f"hii {info["name"] } u done total money of {total} ")    
newpayment(1000,2000,3000,name="santhosh",age="21")  
  #functions without return keyword 
def add(a,b):
   # a+b
    return a+b
print(add(10,20))
#if there are mutiple returns
def add(a,b):
   # a+b
    return a+b
    return a-b
    return a/b 
print(add(10,20))
#we can have mutiple return in differet conditions
def arithmetic(a,b,opr):
    if opr=="+":
        return a+b
    if opr=="/":
        return a/b
    if opr=="*":
        return a*b
    else :
        return "not found"
        print("hiiiiiii")
print(arithmetic(1,2,"-"))
#local variables
def hii():
    a=10
    bb=20
    print(a)
hii()
#print(bb) local variable not defined outside
#passing parameters also local variables only
def add(a,b):
    return a+b
print(add(6,8))
#print(a)
#global variables
cc=99
def add(a,b,cc):
   print(a)
   print(b)
   print(cc)#cc is name conflict
   print(globals()['cc']) #acessing global inside fun when name conflict

add(1,2,3)
print(cc)  #accessing global variable out side fun
#changing global variable
count=0
def add():
    #count+=1
    global count
    count+=1
    
add()
print(count)
#function composition is nothing but function using in another function
def add(a,b):
    return a+b
def sub(c,d,e):
    return add(c,d)-e
print(sub(1,2,3))
#len of string with built in and with out
name="santhu"
print(len(name))
def userdef(s):
    count=0
    for i in s:
        count+=1
    return count
print(userdef("santhu"))
#to check built in functions
#print(dir(__builtins__))
#now using lamda fuctions in one line expressions in terms of how to do what to do
#lambda arguments:expression
sum=lambda a,b :a+b
print(sum)
print(sum(2,3))
#iile immediate invoke lambda function
print((lambda a,b:a+b)(2,3))
#we have functional programming map filter reduce
# now we going to map fun for squarinng
def sqr(n):
    list=[]
    for i in n: 
     list.append(i*i)
    return list
print(sqr([1,2,3,4]))
#now by using map fun    map(function , iterable)
print(list(map(lambda n:n*n , [1,2,3,4])))
#now we go filter fun     filter(function,iterable)
#printing even numbers without filter
def numbers(n):
    list=[]
    for i in n:
        if i%2==0:
            list.append(i)
    return list
print(numbers([1,2,3,4,5,6]))
#by using filter
print(list(filter(lambda n:n%2==0 , [1,2,3,4,5,6])))
#now by using reduce function
#by going factorial
def fact(numbers):
    result=1
    for i in numbers:
        result=result*i
    return result
print(fact([1,2,3,4,5]))
#now by using reduce
from functools import reduce
print(reduce(lambda x,y : x*y , [1,2,3,4,5]))








    





    

    
    
