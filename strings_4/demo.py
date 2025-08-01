#basics bout strings and strig methods
data_1='santhu'
data_2="santhu"
data_3="""santhu"""
data_4='''santhu'''
print(data_1)
print(data_2)
print(data_3)
print(data_4)

python_desc = """Python is a high-level, genera'l-purpose programming language. Its design philosophy emphasizes 
code readability with the use of significant indentation"""
print(python_desc)
question="how are you?"
ans="i'm fine what abot u"
print(ans)
answer="""i'am always"good" """
print(answer)
text="santhosh"
print(text[0])
print(text[5])
print(text[-3])
text="santhoshreddy"
print(text[1:13:1])
print(text[:])
print(text[::3])
print(text[0:4:])
text="iam from siddipet plrp"
print(text[1:22:2]) #a rmsdie lp
text="python"
print(text[-2:-7:-2])
print(text[-4:-1:1]) 
text = "python"
print(text[-3:-6:-1])
text = "python"
print(text[::-1])
print(text[-2:-5:-1])
print(text[-2]+text[-3]+text[-5])
text="python"
#text[0]="P"
text="P"+text[1:]
print(text)
str='hi'
print(str*5)
#string operations or string methods
print(dir(str))
mobile_number=(input("enter mobile number"))
valid_num=mobile_number.isdigit()
print(valid_num)
pan_number=input("enter pan number")
valid_pan=pan_number.isalnum()
pan=pan_number.upper()
print(pan)