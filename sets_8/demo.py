#sets() uuu unique,unordered,unindex
emptyset=set()
print(type(emptyset))
print(emptyset)
#first we go with unordered
set_num={10,20,30,4,5}
print(set_num)
# no duplicates unique data
set_num={10,20,30,4,5,10}
print(set_num)
text_data={"santhu","asr","aksh"}
print(text_data)
#mixed data also we give we get random output
#no indexig  in sets
set_num={10,20,30,4,5,10}
#print(set_num[1])
# no indexing so we acess by converting into list or as it iterable we can get individual elements
set_num={10,20,30,4,5,10}
for i in set_num:
    print(i)
list_num=list(set_num)
print(list_num)
print(list_num[1])    
#add() method adds data randomly if duplicates there replace it 
set_num={10,20,30,4,5,10}
set_num.add(90)
print(set_num)
set_num.add((100,200))
print(set_num)
# update() adds multiple elements iterables only like lists and tuples and sets
set_num={10,20,30,4,5,10}
set_num.update({100,200})
print(set_num)
#remove() method removes the element if found if not found  gives key error but discard method removes if not found no error
set_num={10,20,30,4,5,10}
set_num.remove(10)
print(set_num)
#set_num.remove(100)
set_num.discard(100)
print(set_num)
#clear() and pop() clear will clear whole data and pop will remove random element
set_num={10,20,30,4,5,10}
set_num.clear()
print(set_num)
set_num={10,20,30,4,5,10}
set_num.pop()
print(set_num)
# set related operations mathematical
set_1={10,20,30,40,50}
set_2={40,50,60,70,80}
print(set_1.union(set_2))
print(set_1 | set_2)
print(set_1.intersection(set_2))
print(set_1 & set_2)
print(set_1)
print(set_2)
print("=============================================")
print(set_1.intersection_update(set_2)) #updates the calling set
print(set_1)
print(set_2)
#difference removes elements present in set also
s1={10,20,30,40,50}
s2={40,50,60,70,80}
print(s1.difference(s2))
print(s1-s2)
print(s2-s1)
print(s1)
print(s2)
print(s1.difference_update(s2))
print(s1)
print(s2)
#symmetric difference removes common elements
s1={10,20,30,40,50}
s2={40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1^s2)
print(s2^s1)
print(s1)
print(s2)
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)
#issubset() given set is present in another set or not
s1={10,20,30,40,50}
s2={40,50}
print(s2.issubset(s1))
#superset() set is present or not
s1={10,20,30,40,50}
s2={40,50}
print(s1.issuperset(s2))
#isdisjoint() checks both sets have no common elements
s1={10,20,30,40,50}
s2={40,50}
print(s1.isdisjoint(s2))
#now we go to copy shallow and soft
s1={10,20,30,40,50}
s2=s1.copy()
print(s1)
print(s2)
s2.add(200)
print(s1)
print(s2)
print("==============================")
s1={10,20,30,40,50}
s2=s1
print(s1)
print(s2)
s2.add(200)
print(s1)
print(s2)
#in  frozenset we cant change or update it is immutable only set operations performed
fs=frozenset({1,2,3,4,5})
print(type(fs))
print(dir(frozenset))
fs1=frozenset({20,30,40,50})
fs2=frozenset({200,300,400,50})
print(fs1.union(fs2))