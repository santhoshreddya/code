num_list=[1,2,3,4,5]
print(type(num_list))
print(num_list)
#defining lists with strings
names=["santhu","aarthi","mina","aksh"]
print(type(names))
print(names)
#with list different combination of data
data=[1,2,3,4,5,"santhu","aarthi","mina","aksh"]
print(type(data))
print(data)
#nested list
data=[1,2,3,4,5,["santhu","aarthi","mina","aksh"]]
print(type(data))
print(data)
#using list class
empty_list=list()
print(type(empty_list))
print(empty_list)
num_list=list([1,2,3,4,5])
print(type(num_list))
print(num_list)
#class list is used for only iterable objets
#empty_list=list(10)
#now extractig data from list it is same as strigs like indexing and sicing only
num_list=[1,2,3,4,5,6] 
print(num_list[0])
print(num_list[-4])
print(num_list[:])
print(num_list[::-1])
#now seeing memory address
num_1=10
num_2=10
print(id(num_1))
print(id(num_2))
list_1=[10,20,30]
list_2=[10,20,30]
print(id(list_1))
print(id(list_2))
print(id(list_1[0]))
print(id(list_2[0]))
#so as list is iterable we can use for loop range
num=[1,2,3,4,5,6]
for i in  num:
  print(i)
 #using range print 5 table
cus_list = list(range(0, 26, 5))  # [0, 5, 10, 15, 20, 25]
for i in cus_list:
   print(i * 2)
  
day=["mon","tue","wed","thu","fri","sat","sun"]
inputday=input("enter ur day")
if inputday in day:
  print("exists")
else:
  print("not exist")
  # list methods
num_list=[1,2,3,4,5]
#print(dir(num_list))
#list has 11 methods for operation append used for only one argument
list=[1,2,3,4,5]
print(list)
list.append(6)
print(list)
#for nested list it is added
list.append([10,20])
print(list)
#we can add strings any  thing
list.append("apple")
print(list)
#in extend used for only iterable objects it add as individuals
list_1=[1,2,3,4,5]
print(list_1)
list_1.extend([6])
print(list_1)
list_1.extend("hello")
print(list_1)
#now we go to insert index,value
list_1=[1,2,3,4,5]
print(list_1)
list_1.insert(-2,1)
print(list_1)
list_1.insert(len(list_1),10)
print(list_1)
#pop will remove an index element default remove last element
list_1=[1,2,3,4,5,6,7]
print(list_1.pop())
print(list_1)
list_1=[1,2,3,4,5,6,7]
print(list_1.pop(1))
print(list_1)
print("=====================================================================")
#remove() operates based on value not  on index
list_1=[1,2,3,4,5,6,7,8,7]
print(list_1.remove(7))
print(list_1)
#clear() removes all elements
list_1=[1,2,3,4,5,6,7]
print(list_1.clear())
print(list_1)
#index  returns index value
list_1=[1,2,3,4,5,6,7]
print(list_1.index(4))
print(list_1)
list_1=[1,2,3,4,5,6,7,7,3,4,2,2,1]
print(list_1.index(2,2,12))
print(list_1)
#count fun count and returns number of times the value present
list_1=[1,2,3,4,5,6,7,7,3,4,2,2,1]
print(list_1.count(2))
print(list_1)
#reverse operation reverse the whole list originl list also
list_1=[1,2,3,4,5,6,7,7,3,4,2,2,1]
print(list_1.reverse())
print(list_1)
list_nums = [10,20,30,40,50]
print(list_nums)
print(list_nums[::-1])
print(list_nums)
#sort() will sort the data by defaut ascending order
list_nums = [10,20,60,40,50]
print(list_nums)
print(list_nums.sort())
print(list_nums)
print("---------------------------------------------")
list_nums = [10,30,20,40,50]
print(list_nums)
print(list_nums.sort(reverse=True)) # descending
print(list_nums)
names=["santhu","ramu","arch" ]
names.sort()
print(names)
#it  does not perform mixed data give error
#now we go for copy() shallow copy orignaal not effected
list=[1,2,31,1,2]
print(list)
backuplist=list.copy()
backuplist.append(60)
print(backuplist)
print(list)
#by using assignment operator we do soft copy original effected
list=[1,2,31,1,2] 
print(list)
backuplist=list
backuplist.append(60)
print(backuplist)
print(list)
