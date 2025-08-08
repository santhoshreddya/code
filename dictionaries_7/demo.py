#dictionaries are build in data structures store multiple key value pairs in a single variable
empty_dict={}
print(empty_dict)
print(type(empty_dict))
numbs={1:10,2:20,3:30,4:40}
print(numbs[4])
dict_text={"course1":"python","course2":"java"}
print(dict_text["course2"])
#it also applicable for mixed data
dict_text={"course1":"python","course2":"java",1:10}
print(dict_text[1])
nestdict={101:{"course":"python","age":10},102:{"name":"ramu","age":20,1:30}}
print(nestdict[102])
#as we know keys are immutable if we use key as list we get uhashable error we ue tuple we get ans
numbs={(1,2,3):"python"}
print(numbs[(1,2,3)])
#objects can be any values
numbs={101:["san","sam",21],102:("san","sam",21)}
print(numbs[102])
#update by using assignment operator
names={"name1":"santhu","name2":"karthik"}
names["name3"]="bunny"
print(names)
names["name1"]="sunny"
print(names)
#dict class() works same as list and tuples
numbs=dict({101:["san","sam",21],102:("san","sam",21)})
print(numbs[102])
#update by using assignment operator
names=dict({"name1":"santhu","name2":"karthik"})
names["name3"]="bunny"
print(names)
#now mwthods of dict()
print(dir(dict()))
#update will add items
names={"name1":"santhu","name2":"karthik"}
print(names)
names.update({"name3":"raki"})
print(names)
names.update({"name1":"prabha"})
print(names)
names={"name1":"santhu","name2":"karthik"}
print(names)
#names.pop("name3")
print(names.pop("name1"))
print(names)
#popitem() removes last inserted element
names={"name1":"santhu","name2":"karthik"}
print(names)
names.popitem()
print(names)
#get functin for accessing data
names={"name1":"santhu","name2":"karthik"}
print(names)
print(names.get("name2"))
print(names.get(0)) #it does nt terminate and we not get error
#now we go to keys() it ill return keys only
names={"name1":"santhu","name2":"karthik"}
print(names.keys())
numbs={1:10,2:20,3:30,4:40}
print(numbs.keys())
only_keys=numbs.keys()
for i in only_keys:
    print(i)
#values() returns only values
numbs={1:10,2:20,3:30,4:40}
print(numbs.values())
only_values=numbs.values()
for i in only_values:
    print(i)
#items() returns both keys and values
numbs={1:10,2:20,3:30,4:40}
print(numbs.items())
#copy() 2 types shallow copy and soft copy()
numbs={1:10,2:20,3:30,4:40}
bk_copy=numbs.copy()
bk_copy.update({"name":"santhu"})
print(bk_copy)
print(numbs)
#soft copy
numbs={1:10,2:20,3:30,4:40}
bk_copy=numbs
bk_copy.update({"name":"santhu"})
print(bk_copy)
print(numbs)
#setdefault() if key already present it will not update 
numbs={1:10,2:20,3:30,4:40}
numbs.setdefault(5,500)
print(numbs)
numbs.setdefault(1,100)
print(numbs)
#for duplicates it allows but if key is presnt it updates key values
numbs={1:10,2:20,3:30,4:40,1:1000}
print(numbs)

