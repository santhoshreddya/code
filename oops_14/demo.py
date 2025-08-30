#now we are going with oops so class is a blue print of object and object is instance of class by using object we can get data of class class contains data and statements
class student:
    #class contains data or variables or attributes
    student_name="santhosh"
    student_email="santhoshreddya5553@gmail.com"
    #now statements
    print(student_name,student_email)
student_obj=student()
#print(student_obj)
#we can get data by using student_obj object
print(student_obj.student_name)
print(student_obj.student_email)
print("="*50)
#now we are going with methods
class student:
    #class contains data or variables or attributes
    student_name="santhosh"
    student_email="santhoshreddya5553@gmail.com"
    #self is object by defauly it takes first parameter as object now we can get by using object
    def info(self):   #we give any parameter it considers first parameter as current object
     print(self.student_name,self.student_email)
    # print(student.student_name,student.student_email)  by using class name also valid
#these down data is same method we getting by diff obj same data  we getting hardcoaded data
student_one=student()
student_one.info()
student_two=student()
student_two.info()
student_three=student()
student_three.info()
print("="*50)
#now we want data dynamic we go special keyword call __init__ constructor
class student:
    student_name="santhosh"
    student_email="santhoshreddya5553@gmail.com"
    def __init__(self,student_name,student_email): #instance variables constructor use for initializing data
       print(student_name)
       print(student_email)
student_obj=student("santhu","santhu@gmail.com")
print("="*50)
class student:
    
    def __init__(self,student_name,student_email): #instance variables constructor use for initializing data
       #print(student_name)
       self.student_name=student_name # these are called instance variables
       self.student_email=student_email
    def fun(self):
       print("studntname is " ,self.student_name)
       print("studntemail is " ,self.student_email)
      
student_one=student("santhu","santhu@gmail.com")
student_two=student("chintu","chintu@gmail.com")
student_one.fun()
student_two.fun()