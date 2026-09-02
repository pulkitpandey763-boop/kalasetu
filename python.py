# x=input("Enter num1")
# y=input("Enter num2")
# z=x+y
# print(z)
# print(type(z))

# x=int(input("Enter num1"))
# y=int(input("Enter num2"))
# z=x+y
# print(z)
# print(type(z))

# a=10
# b=10
# c=10
# print(id(c))
# print(id(a))
# print(id(b))

# a=10
# print(type(a),a,id(a))

#IMMUTABLE
# x=10
# print(x)
# print(id(x))
# x=x+1
# print(x)
# print(id(x))

# complex
# a=3+4J
# print(a)
# print(id(a))
# print(type(a))

# a=4+3J
# print(a)
# print(id(a))
# a=a+1
# print(a)
# print(id(a))

#BOOL true
# a=5>3
# print(a)
# print(type(a),a)

#Bool false
# a=5<3
# print(type(a),a)

# x=None
# print(x==None)
# print(x==10)

# my_str="hello world"
# print(id(my_str))
# my_str=my_str+"world"
# print(id(my_str))

# my_str="hello"
# my_str=my_str+"world"
# print(my_str)

# print('abcd\n')
# print("abcd\n efgh\n ijklm\n nopq\n rst uv\n wx\n yz\n")
# print("A-143\n sovereign tower\n sectoe-124,Noida ")
# print("ab\n cd\\tn ef\n")
# print("ab\\t cd\n efg\\t hi\n")
# print("ab\t cd\n efg\t hi")
# print("ab\t cd\t gh")
# print(r"ab\t gh\n ij\t kl ")

#separator string
# print(10,20,30.5,"hi")
# print(10,20,30.5,'hi',sep=",")
# print(10,20,30.5,"hi", sep="$") 
# print(10,20,30.5,"hi", sep="%")
# print(10,20,30.5,"hi", sep="\t")
# print(10,20,30.5,"hi", sep="\n")
# print(10,20,30.5,"hi", sep="None")
# print(10,20,30.5,"hi", sep="\n \t")
# print(10,20,30.5,"hi", sep=None)

#end string
# print("pulkit","angad","hanuman",end =",")
# print("tagdu","tonda",end = ";")
# print("hi","hello","bye",sep="\n",end = "hello")
# print("Apple",end=",")
# print(end="#")
# print(sep="$", end="\t")
# print(2023)

# !IMPO0RTANT tripple quotes as a string
# a=("'now this line will be considered as a executable program and this will be stored in a memory so we can use it'")
# print(a)

# !NOTE TRIPPLE QUOTE AS COMMENT
# "' NOW THE TRIPPLE QUOTE STRING IS CONSIDERED AS A COMMENTR BECAUSE THERE IS NO VALUE WHICH IS ASSIGNED TO THIS TRIPPLEW QUOTE STRING THATS WHY IT WILL BE TAKEN AS NON EXECUTABLKE PROGRAM '"

# 
# name=("rolex")
# age=77
# price=(60)
# print(name)
# print(age)
# print(price)
# print(type(name),type(age))

# pulkit=(True)

# a=20
# b=89
# pulkit=a+b
# print(pulkit)

# kan=a-b
# print(kan)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b) #power operator
# print(a % b) #modulur operator

# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# num=10
# print(num+10)

# name=input("tell me ur number")
# print("welcome", name)
# print(type(name),name)

# !problem 1

# num=int(input("enter your first number "))
# num2=int(input("enter your second number"))
# sum=num+num2
# print(sum)
     
# !probelm 2 area of a square

# side=float(input("type your side of a square sir"))
# print("area=",side*side)

# !probelm 3 average of a two numbers

# num1=float(input("type ur number 1 :"))
# num2=float(input("type ur number 2 :"))
# num3=(num1+num2)
# num4=(num3/2)
# print("average=",num4)

# ! problem 4 true or false 
# a=50
# b=30
# print(a>=b)
# print(a<=b)

#!length and indexing
# str="pulkit"
# print(str[4])
# print(len(str))

#!concatenation
# str1="pul"
# str2="kit"
# str=(str1+str2)
# print(str)

# #! functions
# str="we are pro"
# print(str.endswith("pro"))
# print(str.startswith("we"))
# print(str.replace("pro","noob"))
# print(str.capitalize())
# print(str.find("r"))
# print(str.count("r"))

#!probelm 1
# name=str(input("write the fisrt name sir :"))
# print(len(name))

#! problem 2
# str="I earn in dollars $"
# print(str.find("$"))
# print(str.count("$"))

#!conditional statement if
# age=24
# if(True):
#     print("can vote","\n can drive" )

#! elif

# sport="volleyball"

# if(sport=="kabaddi"):
#     print("play")
# elif(sport=="volleyball"):
#     print("true")
# elif(sport=="cricket"):
#     print("false")

# print("end of the code")

#! problem on result 

# marks=float(input("type ur marks sir:"))
# if(marks>=90):
#     print("grade=A")
# elif(90>marks>=80):
#     print("grade=B")
# elif(80>marks>=70):
#     print("grade=c")
# else:
#     print("grade is D")

#!problem on even and odd 
# num=float(input("write ur number:"))
# if(num%2==0):
#     print("the number is even")
# else:
#     print("the number is odd")

# #! problem on greatest of three number 
# num1=float(input("write ur first number:"))
# num2=float(input("write ur second number:"))
# num3=float(input("write ur third number:"))
# if(num2<num1>num3):
#     print("the greatest number is this",num1)
# elif(num1<num2>num3):
#     print("the greatest number is this",num2)
# elif(num1<num3>num2):
#     print("the greatest number is this",num3)
# elif(num1==num2==num3):
#     print("all the given numbers are same")
# elif:
#     print("print the two values are smallest from the given 3 number that is",num1,num3)

#! probem on multiple of 7
# num=float(input("write ur number:"))
# if(num%7==0):
#     print("it is the multiple of 7")
# else:
#     print("it is not a multiple of 7")

# marks=[22,33,6,45]
# print(len(marks))
# print(marks[0])
# print(marks[0]==56)
# marks[0]=56
# print(marks[:3])
# print(marks.append(7)) #append function
# print(marks.sort())    # sort function 
# print(marks.insert(2,90)) #insert function
# print(marks)

#! tuple 
# tup=(1,2,3,3,3,4,4,1,2,4,6,)
# print(tup.count(1))
# print(tup.index(1))

#!proble 1

# movies=[]
# movie1=str(input("name of first movie"))
# movie2=str(input("name of second movie"))
# movie3=str(input("name of third movie"))
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)

#! problem 
# list1=[1,2,2,1]
# list2=[1,2,3,4]
# copy_list1=list1.copy()
# copy_list1.reverse()
# copy_list2=list2.copy()
# copy_list2.reverse()
# if(copy_list1==list1):
#     print("list 1 palindrome")
# elif(copy_list1!=list1):
#     print("list 1 not palindrome")
# if(copy_list2==list2):
#     print("list2 palindrome")
  
# else:
#     print("list2 not palindrome")
     

# list=["C","D","A","A","B","B","A"]
# print(list.sort(reverse=True))
# print(list)
     
#! dictionary
# dict={
#     "name":"RAHUL",
#     "SUBJECTS" : {
#         "physics": 45,      
#         "chemistry" : 90,
#         "maths" : 44,
#     }
# } #nested
# print(dict)
# print(dict.keys())

#! probelem on dictionary
# dictionary={
#     "cat" : "a small animal",
#     "table" : ("a peice of furniture","lists of facts and figures")
    
# }
# print(dictionary)

#! problem 2 
# set={"java","java","python","python","c++","c++","c","javascript"}
# print(set)
# print(len(set))

#! problem 2
# marks={}

# x=int(input("ur physics marks"))
# marks.update({"physics":x})

# y=int(input("ur chem marks"))
# marks.update({"chem":y})

# z=int(input("ur maths marks"))
# marks.update({"maths":z})

# print(marks)


l=["riya","priya","shubhi","shubham","naina"]
i=0
while(i<len(l)):
    print(l[i])

    i=i+1
   
















































































































































































































