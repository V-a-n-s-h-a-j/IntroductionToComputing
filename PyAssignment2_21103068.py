                                            #INTRODUCTION TO COMPUTING
                                                   #ASSIGNMENT-2
#Vanshaj
#21103068
#CSE
#INTRODUCTION TO COMPUTING


#Q1
given="Python is a case sensitive language"
#1A)
print("The length if the string is : ",len(given),"\n")

#1B)
newGiven_1=given[::-1]
print(newGiven_1,"\n")

#1C)
newGiven_2=given[10:27]
print(newGiven_2,"\n")

#1D)
newGiven_3=given.replace("a case sensitive","an object oriented")
print(newGiven_3)

#1E)
given.find("a",)
print("\n")

#1F)
newGiven_4=given.replace(" ","")
print(newGiven_4,"\n")


#2
name=str(input("Enter name: "))
sid=int(input("Enter SID: "))
depName=str(input("Enter Department Name: "))
cgpa=float(input("Enter CGPA: "))
#Takes input of different credentials

print("Hey, %s Here!" %name)
print("My SID is %d"%(sid))
print("I am from %s department and my CGPA is %f \n" %(depName,cgpa) )


#3
a=56
b=10
#3A)
print("Bit wise AND operator gives: ",a&b,"\n")

#3B)
print("Bitwise OR operator gives: ",a|b,"\n")

#3C)
print("Bitwise XOR operator gives: ",a^b,"\n")

#3D)
print("Left shift of a gives: ", a<<2)
print("Left shift of b gives: ", b<<2,"\n")

#3E)
print("Right shift of a gives: ", a>>2)
print("Right shift of b gives: ", b>>4)


#4
int1=int(input("Enter an integer: "))
int2=int(input("Enter an integer: "))
int3=int(input("Enter an integer: "))
maxx=[int1,int2,int3]
print("Greatest integer is : ",max(maxx),"\n")


#5
string=str(input("Enter a sentance: "))
if "name" in string:
    print("Yes\n")
else:
    print("No\n")


#6
len1=input("Enter length: ")
len2=input("Enter length: ")
len3=input("Enter length: ")
if(len1>=len2+len3 or len2>=len3+len1 or len3>=len1+len2):
    print("Triangle cannot be formed")
else: 
    print("Triangle can be formed")