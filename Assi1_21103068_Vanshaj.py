                                                  # INTRODUCTION TO COMPUTING
                                                         # ASSIGNMENT-1
# VANSHAJ
# SID - 21103068
# CSE

#Q1
num1=float(input("Enter number 1"))
num2=float(input("Enter number 2"))
num3=float(input("Enter number 3"))

avg=(num1+num2+num3)/3.0   #Calculates average of the numbers

print(avg)

#Q2
grossIncome=float(input("Enter gross income"))
dependents=int(input("Enter no. of dependants"))
stdDeduction=10000

taxableIncome=grossIncome-stdDeduction-dependents*3000  #Calculates the taxable income

tax=taxableIncome*20/100  #Calculates tax to be paid

print("Income tax to be paid is : $",tax)

#Q3

SID=int(input("Enter SID"))
name=str(input("Enter name"))
gender=str(input("Enter M if male, F if female, U if unknown"))
course=str(input("Enter course name"))
cgpa=float(input("Enter CGPA"))
student=[SID,name,gender,course,cgpa]
print(student)

#Q4

std1=float(input("Enter marks of student 1"))
std2=float(input("Enter marks of student 2"))
std3=float(input("Enter marks of student 3"))
std4=float(input("Enter marks of student 4"))
std5=float(input("Enter marks of student 5"))
marksList=[std1,std2,std3,std4,std5]
marksList.sort()
print(marksList)

#Q5 a)
colours=['red','green','white','black','pink','yellow']
colours.pop(3)     #Removes the 4th element
print(colours)

#Q5 b)
colors=['red','green','white','black','pink','yellow']
colours[3:5]=['purple']    #Replaces 4th and 6th element with purple
print(colours)


