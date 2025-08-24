#normally all we used is for ram temporary storage data output not permanent storage data we go with files
#1st syntax
# open ("file path",mode)
#mode===  rwa
file=open("file.txt","r")
#print(type(file))
print(file)
print(file.closed)
file.close()
print(file.closed)
#2nd syntax when the file is not closed leaked of some data
with open("file.txt","r") as file_new:
   #print(type(file))
   print(file)
#print(file_new.closed)
  #print(file_new.read())
  #print(file_new.readline())
  #for i in file_new.read():
   # print(i)
  #print(file_new.readlines())
  #for i in file_new.readlines():
   # print(i.strip())
 #for creating a new file then  
with open("new.txt","w") as new_file:
  #print(new_file)
  #default it override data
  new_file.write("hi im santosh im fine")
  # for writting multiple lines of data we go with writelines()
with open("data.txt","w") as new_file:
   new_file.writelines(["hi im santhosh\n","im vce\n"])
#now we go to append mode of operation it will add exiting data not overwrite data
with open("data.txt","a") as new_file:
   new_file.writelines(["hi im arthi\n","im grrr\n"])
with open("del.txt","w") as new_file:
   new_file.writelines(["hi im arthi\n","im grrr\n"])   
import os
os.remove("del.txt")
#now we are going with csv modules 
import csv
with open("base_module.csv","r") as new_file:
   csv_reader=csv.reader(new_file)
   print(csv_reader)
   for i in csv_reader:
     # print(i)
      if i[3]=="hyderabad":
         print(i)
      if i[2].endswith("@gmail.com"):
         print(i)
with open("base_module.csv","r") as new_file:
   csv_reader=csv.DictReader(new_file)
   print(csv_reader)
   for i in csv_reader:
      if i["email"].endswith("@gmail.com"):
         print(i)
with open("new_module.csv","w") as new_file:
   csv_writer=csv.writer(new_file)
   print(csv_writer)
   csv_writer.writerow(["name","email","phone","address"])
   csv_writer.writerow(["santhu","santhu@gmail.com","9666565553","plrp"])
   csv_writer.writerows([["santhu","santhu@gmail.com","9666565553","dbk"],["santhu","santhu@gmail.com","9666565553","sdpt"]])
with open("new_module.csv","a") as new_file:
   csv_writer=csv.writer(new_file)
   print(csv_writer)
   csv_writer.writerow(["name","email","phone","address"])
   csv_writer.writerow(["santhu","santhu@gmail.com","9666565553","plrp"])
   csv_writer.writerows([["santhu","santhu@gmail.com","9666565553","dbk"],["santhu","santhu@gmail.com","9666565553","sdpt"]])
import json
student={
   "id":101,
   "name":"santhu",
   "course":"python full stack",
   "score": 7.5,
   "skills":["python","java","django"]
}
with open("write_json","w") as new_file:
   json.dump(student,new_file,indent=4)
#now for reading the data
with open("write_json","r") as new_file:
   json_read=json.load(new_file)
   print(json_read)
   print(json_read["name"])
   print(json_read['skills'][0])
#converting python json dic to python string
student_json=json.dumps(student)
print(student_json)
#now converting string to json
stu_data='{"id": 101, "name": "santhu", "course": "python full stack", "score": 7.5, "skills": ["python", "java", "django"]}'
print(type(stu_data))
stu_json=json.loads(stu_data)
print(type(stu_json))






