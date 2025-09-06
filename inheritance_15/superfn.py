#now we going to different fns
class person():
    def __init__(self,person_id,person_name,person_age):
        self.person_id=person_id
        self.person_name=person_name
        self.person_age=person_age
    def display_info(self):
        print(f"id = {self.person_id}")
        print(f"name = {self.person_name}")
        print(f"age = {self.person_age}")
class student(person):
    def __init__(self,student_id,student_name,student_age):
        super().__init__(student_id,student_name,student_age)
    
class trainer(person):
    def __init__(self,trainer_id,trainer_name,trainer_age,trainer_disc):
        super().__init__(trainer_id,trainer_name,trainer_age)
        self.trainer_disc=trainer_disc
    def display_info(self):
        super().display_info()
        print(f"trainer discription is {self.trainer_disc}")
obj1=student(101,"santhosh","22")
obj1.display_info()
obj2=trainer(102,"aksh",22,"data analytics")
obj2.display_info()

    