name= "I am java trainer"
print(name)


print("-------------------------------------")

#slicing in string
print("slicing in string")
print("name[2:4]", name[2:4])
print("name[5:9]", name[5:9])
print("name[:15]", name[:15])
print("name[2:]", name[2:])
print("name[:]", name[:])
print("name[0:17:3]", name[0:17:3])
print("name[::]", name[::])
print("name[::-1]", name[::-1])


print("-------------------------------------")

#is operator in string
print("is operator in string")
x=["apple", "banana"]
y=["apple", "banana"]
z=x
print(x is z)
print(x is y)


print("-------------------------------------")

#capitalize() in string
print("capitalize() in string")
str = "rahul tiwari"
print(str)
print(id(str))
str.capitalize()
print(str)
print(id(str))
str1=str.capitalize()
print(str1)
print(id(str1))


print("-------------------------------------")

#center() in string
print("center() in string")
str="rahul"
print(str)
str=str.center(15,"*")
print(str)
str="Hello"
str2=str.center(20)
print("Old value:",str)
print("New value:",str2)


print("-------------------------------------")

#count() in string
print("count() in string")
str="second a start index and third"
str0 = str.count('a')
print(str0)
str1 = str.count("a",8)
print(str1)
str2 = str.count("a",8,15)
print(str2)


print("-------------------------------------")

#endswith() in string
print("endswith() in string")
str="second a start index and third"
isends= str.endswith("and")
print(isends)
isends1= str.endswith("d")
print(isends1)
isends2= str.endswith("nd",0,6)
print(isends2)


print("-------------------------------------")

#find() in string
print("find() in string")
str=("Welcome to python class.")
str2=str.find("t")
print(str2)
str1= str.find("too",9,13)
print(str1)


print("-------------------------------------")

#index() in string
print("index() in string")
str=("Welcome to python class.")
str1=str.index("th",0,21)
print(str1)


print("-------------------------------------")

#isalnum() in string
print("isalnum() in string")

str=("Welcome to python class.")
output= str.isalnum()
print(output)

str1=("Welcome.")
output1=str1.isalnum()
print(output1)

str2=("welcome")
output2=str2.isalnum()
print(output2)



print("-------------------------------------")

#isalnum() in string
print("isalnum() in string")

str=("Welcome to python class.")
output= str.isalnum()
print(output)

str1=("Welcome.")
output1=str1.isalnum()
print(output1)

str2=("welcome")
result=str2.isalnum()
print(result)



print("-------------------------------------")


#strip(), lstrip(), rstrip() in string
print("strip(), lstrip(), rstrip() in string")

str="    rahul"
print(str)
str1=str.lstrip()
print(str1)

STR="-------Rahul------"
STR1=STR.lstrip('-')
print(STR1)

STR2=STR.rstrip('-')
print(STR2)
STR3=STR.strip('-')
print(STR3)


print("-------------------------------------")

#replace() in string
print("replace() in string")

str= "java is a programming language"
str1= str.replace("java","C")
print("Old String :\n",str)
print("New String :\n",str1)


print("-------------------------------------")


#swapcase() in string
print("swapcase() in string")

str= "HELLO Rahul"
str1=str.swapcase()
print(str1)


