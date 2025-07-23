#arithmetic operators
a=5
b=7
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)#floor case
print(a**b) #5^7
#compound assignment operators
num=10
num +=1
print(num)
#comparisional or relational operators
num1=9
num2=9
print(num1>num2)
print(num1<num2)
print(num1!=num2)
print(num1==num2)
print(num1>=num2)

#logical operators
a=10
b=20
c=21
d=15
res_and=a > b and c>d
print(res_and)
res_or=a > b or c>d
print(res_or)
res_not=not a > b 
print(res_not)
#membership operators
text="santhosh reddy"
h_present="h" in text
print(h_present)
h_notpresent="b" not in text
print(h_notpresent)
#identity operators campare objects on memory level
a=10
b=10
print(a is b)
print(a is not b)
c=[1,2,3,4,5]
d=[1,2,3,4,5]
print(c is d)
print(c is not d)
#bitwise operators
a=5
b=3
resultand=5&3
print(resultand)
resultor=5|3
print(resultor)
resultxor=5^3
print(resultxor)
resultnot=~3
print(resultnot)

print(3<<2) #12
print(3>>2) #0







