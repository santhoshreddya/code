#when there are errors abtruption
print("program execution started")
a=10
b=20
print(a/b)
print("program execution closed ")
print("="*50)
#if there are errors how python handles them how intrupt the code
print("program execution started")
a=10
b=9
print(a/b)
print("program execution closed ")
print("="*50)
#if there are errors how we handle them
print("program execution started")
a=10
b=0
try:
 print(a/b)
except:
 print("we cannot divide by 0 in mathematic in python")

print("program execution closed ")
print("="*50)
#if there are multiple errors in code 

print("program execution started")
import sys
data=[1,2,"python",0,"santhu",9]
print(sys.exc_info)

for i in data:
 try:
  print(1/i)
 except ZeroDivisionError:
  print("we cannot divide by 0 in mathematic in python")
 except TypeError:
  print("we cant devide by strings")

print("program execution closed ")
print("="*50)
#print(dir(sys.exception()))
print("program execution started")
num1=10
num2=0
try:
 print(num1/num2) #verifying login info
except :
 print("devide by zero does nt exist")
else:
 print("verify with otp") #when verified login info
finally:
 print("program executed finally")
print("program execution closed")
print("="*50)
#for  custom exception on my own
class invalidscoreerror(Exception):
 pass
try:
 score=int(input("enter ur score btwn 0-100 :"))
 if score<0 or score >100:
  raise invalidscoreerror
 print("score valid")
except invalidscoreerror as e:
 print("score must between 0-100",e)
print("="*50)

class tooyoungage(Exception):
 pass
class noiderror(Exception):
 pass
try:
 age=int(input("enter ur age "))
 has_id=input("has id or not yes or no")
 if age<18:
  raise tooyoungage
 if has_id!="yes":
  raise noiderror
 print("ur eligible")
except tooyoungage:
 print("ur age must be greater than 18")
except noiderror:
 print("u does nt have id")
else:
 print("registration sucessfull")
print("="*50) 


