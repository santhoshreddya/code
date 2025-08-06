#tuples
empty_tuple=()
print(type(empty_tuple))
print(empty_tuple)
my_tuple=(1,2,3,4,5)
print(type(my_tuple))
print(my_tuple)
#mixed tuple
tuple_2=(1,2,3,4,5,"ant","reddy",3.2)
print(type(tuple_2))
print(tuple_2)
print("===========================================")
#by using tuple_class
empty_tuple=tuple()
print(type(empty_tuple))
print(empty_tuple)
tuple_1=tuple([1,2,3,4,5])
print(type(tuple_1))
print(tuple_1)
numbers=tuple(("hello","hi",1,2,3.14))
print(type(numbers))
print(numbers)
#tuple_int = tuple(10) 
#tuple_int = tuple((10)) 
tuple_int = tuple((10,))
print(tuple_int)
list_nums = [10,20,30,40,50]
print(list_nums)
tuple_nums=tuple(list_nums)
print(tuple_nums)
list_nums = list(tuple_nums)
print(list_nums)
#accessig data in tuples by indexing
tuple_nums=(1,2,3,4,5)
print(tuple_nums[1])
print(tuple_nums[-1])
#by slicing accesing
tuple_nums=(1,2,3,4,5)
print(tuple_nums[1:4])
print(tuple_nums[4:1:-1])
#looping is done it iterable
tuple_nums=(1,2,3,4,5)
for i in tuple_nums:
 print(i)
 #by using range 
tuple_nums=tuple(range(0,26,5))
print(tuple_nums)
#performing any operations with tuples
tuple_nums=tuple(range(0,26,5))
for i in tuple_nums:
 print(i*2)
days = ("sun","mon","tue","wed","thu","fri","sat")
day = input("Enter day name in a week: ")
if day in days:
    print("Day Exists")        
else:
    print("Invalid Day In Week")        

# Duplicates are allowed
tuple_nums = (10,20,30,40,50,50,50,30)  
print(tuple_nums)
#print(dir(tuple()))
# tuple operations'count', 'index']
tuple_nums = (10,20,30,40,50,50,50,30)  
print(tuple_nums.index(30))
print(tuple_nums.count(50))
#now tuple packing and un packing
names=("santhosh","mahesh","chintu","kavi")
name1,name2,name3,name4=names
print(name1)
print(name2)
print(name3)
print(name4)
t1=([10,20],[30,40],[50,60])
t1[0][0]=100
print(t1)
#t1[0]=[20,30]
l1=[(10,20),(30,40),(50,60)]
l1[0]=(20,30)
print(l1)
#l1[0][0]=200
print(l1)
