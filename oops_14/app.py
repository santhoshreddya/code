#now we go with class variables instance variables instance methods 
class student:
    institute_name="digital edify"  #class variables
    def __init__(self,student_name,student_email):
        self.student_name=student_name  #by using constructor we create instance variables
        self.student_email=student_email
        #now instance method
    def info(self):
        print("welcome to " , student.institute_name)
        print("student name is " , self.student_name)
        print("student email" ,self.student_email)
        local_var=20
        print(local_var)
        #now to change class level data we go to class level methods
    @classmethod
    def change_institutename(cls,new_name):
        cls.institute_name=new_name
    @staticmethod
    def check_email(email):
        return "@" in email and "." in email
student_one=student("santhu","reddy@6662@gmail.com")
student_two=student("akssh","aaksh@gmail.com")
student_one.info()
student_two.info()
student.change_institutename("q spiders")
print(student.check_email("santhoshreddya5553@gmail.com"))



        
