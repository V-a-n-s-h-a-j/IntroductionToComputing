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
#len() gives length of the string

#1B)
newGiven_1=given[::-1]
#reverses order of the string
print(newGiven_1,"\n")


#1C)
newGiven_2=given[10:27]
#stores elements of given in a new string variable
print(newGiven_2,"\n")

#1D)
newGiven_3=given.replace("a case sensitive","an object oriented")
#replaces some elements with new elements
print(newGiven_3)

#1E)
given.find("a",)
#finds the index of 'a' in the given string
print("\n")

#1F)
newGiven_4=given.replace(" ","")
#removes the spaces between words
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
# % is used to enter the credentials in appropriate places


#3
a=56
b=10
#3A)
print("Bit wise AND operator gives: ",a&b,"\n")
# & operator used to find bitwise AND relation between a,b

#3B)
print("Bitwise OR operator gives: ",a|b,"\n")
# | operator used to find bitwise OR relation between a,b

#3C)
print("Bitwise XOR operator gives: ",a^b,"\n")
# ^ operator used to find bitwise XOR relation between a,b

#3D)
print("Left shift of a gives: ", a<<2)
print("Left shift of b gives: ", b<<2,"\n")
# << left shifts the bit value of a and b

#3E)
print("Right shift of a gives: ", a>>2)
print("Right shift of b gives: ", b>>4)
#<< and >> left shift and right shift the values of a and b respectfully


#4
int1=int(input("Enter an integer: "))
int2=int(input("Enter an integer: "))
int3=int(input("Enter an integer: "))
maxx=[int1,int2,int3]
print("Greatest integer is : ",max(maxx),"\n")
#max() finds the maximum value in the list


#5
string=str(input("Enter a sentance: "))
if "name" in string:
#checks whether the string "name" is present in the input string or not
  print("Yes\n")
else:
    print("No\n")


#6
len1=input("Enter length: ")
len2=input("Enter length: ")
len3=input("Enter length: ")
if(len1>=len2+len3 or len2>=len3+len1 or len3>=len1+len2):
#checks the basic triangle forming condition i.e. length of any one side shouldnt be greater than the sum of lengths of the other two sides 
    print("Triangle cannot be formed")
else: 
    print("Triangle can be formed")
