#Q1
print("1)")
string=input("Enter a string: ")
occ={} #Empty dictionary
if " " in string:
    words=string.split(" ") #Splits the words in the string into a list
    for i in words: 
        if i in occ: #Checks if the word is in the disctionary or not
            occ[i] += 1 #iterates the word if it is already present in the dictionary
        else:
            occ[i]=1 #adds the word to the dictionary
    print("Occurences of words in your sentence: ",occ)
else:
    letters=list(string) #stores the letters of a word in a list
    for i in letters: 
        if i in occ: #checks if the letter is in the dictionary
            occ[i] += 1 #iterates the letter  
        else:
            occ[i]=1 #adds the letter to the disctionary
    print("Ocuurences of letters in your word: ",occ)
print("\n")

# Q2
print("2)")
date = int(input("Enter date: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
if date > 31 or date <= 0: #Max 31 days in all months
    print("ERROR: value of date cannot be ", date) 
elif month > 12 or month < 1: #Max 12 months
    print("ERROR: value of month cannot ", month)
elif year > 2025 or year < 1800: 
    print("ERROR: value of year cannot be ", year)
else:
    if year%4 != 0: #If this is true, then the year is a normal year (not a leap year)
        if month==2: #Month that has 28 days
            if date>28: #Since february has 28 days in normal years unlike other months
                print("ERROR: value of date cannot be ",date)
            else:
                if date == 28: #Month changes after 28th
                    date = 1
                    month += 1
                else: #For the days that don't affect the change in the month
                    date += 1
                print("The next date is : %d/%d/%d" % (date, month, year))  
        elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12: #Months that have 31 days
            if date == 31 and month == 12: #For the last day of the year
                date = 1
                month = 1
                year += 1
            elif date == 31 and month != 12: #For the last day of a month
                date = 1
                month += 1
            else: #For a day that doesn't affect the change in month or year
                date += 1  
            print("The next date is : %d/%d/%d" % (date, month, year))     
        else: #For the months that have 30 days
            if date>30 or date<1: #Max 30 days
                print("ERROR: value of date cannot be ",date)
            else:
                if date == 30: #For the last day of the month
                    date = 1
                    month += 1
                else:  #For the days that don't affect the change in month or year
                    date += 1
                print("The next date is : %d/%d/%d" % (date, month, year))
    else: #The following lines of code are for the leap years
        if month==2: #February has less number of days wrt other months
            if date>29: #February has 29 days in a leap year unlike 28 days in normal years
                print("ERROR: value of date cannot be ",date)
            else:
                if date == 29: #For the last date of the month
                    date = 1
                    month += 1 
                else: #For the days that don't affect the change in month
                    date += 1
                print("The next date is : %d/%d/%d" % (date, month, year))  
        elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12: #Months with 31 max days
            if date == 31 and month == 12: #For the last date of the year
                date = 1
                month = 1
                year += 1
            elif date == 31 and month != 12: #For the last date of the month
                date = 1
                month += 1
            else: #For the days that don't affect the change in month
                date += 1  
            print("The next date is : %d/%d/%d" % (date, month, year))     
        else:
            if date>30 or date<1: #Max 30 days
                print("ERROR: value of date cannot be ",date)
            else:
                if date == 30: #Last day of the month
                    date = 1
                    month += 1
                else: #For the days that don't affect the change in month
                    date += 1
                print("The next date is : %d/%d/%d" % (date, month, year))
print("\n")


#Q3
print("3)")
terms=int(input("Enter number of terms : "))
num=[] #Creating an empty list
for i in range(terms): #This loop will take the input numbers
    temp=int(input('Enter Number: '))
    num.append(temp)
print("Your input: ",num) #Prints input

sq_num=[] #Empty list
for j in num: #The loop will append a tuple of each input value and its square
    sq_num.append((j,j**2))
print("Output: ",sq_num)
print("\n")


#Q4
print("4)")
gradePoint=int(input("Enter your grade points: "))
if gradePoint<4 or gradePoint>10: #The range of the gradepoints is (4,10)
    print("ERROR: Grade points cannot be ",gradePoint)
else: #The gradepoint is within the range
    if gradePoint==4:
        letterGrade="D"
        perf="Poor"
    elif gradePoint==5:
        letterGrade="C"
        perf="Below Average"
    elif gradePoint==6:
        letterGrade="C+"
        perf="Average"
    elif gradePoint==7:
        letterGrade="B"
        perf="Good"
    elif gradePoint==8:
        letterGrade="B+"
        perf="Very Good"
    elif gradePoint==9:
        letterGrade="A"
        perf="Excellent"
    else:
        letterGrade="A+"
        perf="Outstanding"
    print("Your grade is %s and %s Performance."%(letterGrade,perf))
print("\n")
        
#Q5
print("5)")
word="ABCDEFGHIJK"
space=" "
print(word)
for i in range(len(word)//2+1): #The number of times the function will execute is 1 more than the integer value of half the length of the word
    word=word[:len(word)-2] #len(word)-2 will remove the last 2 letters of the word with each loop
    print(" "*i,word) # (" "*i) will increase the number of spaces with each loop so that the last letter/letters are centered
print("\n")

#Q6
print("6)")
cred_SID=dict() #creates empty dictionary
cred_Name=dict() #creates another empty dictionary

while True:
    
    sid=int(input("Enter a unique SID: "))
    name=str(input("Enter name: "))
    cred_SID[sid]=name #enters names of students in cred_SID with sid as the key
    cred_Name[name]=sid #enters sid of students in cred_Name with name as the key
    again=str(input("Enter 'Y' if you want to continue inputting names and SIDs \nEnter 'N' if you're done "))
    again=again.upper() #this method changes the lower case alphabets to upper case alphabets
    if again=='Y': #the loop will run again if value of again is 'Y'
        continue
    elif again=='N': #the loop will not run again if value of again is 'N'
        break
    else:
        cred_SID={} #resets the cred_SID dictionary since the value of again is not matched with 'Y' or 'N'
        cred_Name={} #resets the cred_Name disctionary like cred_SID
        print("ERROR: Enter 'Y' or 'N' only. Rerun the program.")
        break

print("6a)")
print(cred_SID)

print("6b)") 
for key in sorted(cred_Name): #Sorts the dictionary in an alphabetical order of student names
    print(key, cred_Name[key])

print("6c)")
for key in sorted(cred_SID): #Sorts the dictionary in the increasing order of SIDs
    print(key, cred_SID[key])

print("6d)")
key=int(input("Enter the SID: "))
if key in cred_SID: #Runs if the SID is present in the dictionary 
    print("Name: ",cred_SID[key])
else: #Runs if the SID is not present in the dictionary
    print("The SID entered does not exist. ")
print("\n")

#Q7
print("7)")
n=int(input("Enter the number of terms of the fibonacci sequence: "))
sum=0 #This will be required for the average of the series

a=0 #The first value of the fibonacci sequence
b=1 #A temporary variable which helps getting the sequence correct
for i in range(n):
    print(a)
    c=a+b
    sum+=a
    a=b
    b=c
avg=sum/n #Calculates the average of the series
print("The average of the above fibonacci series is: ",avg, "\n")

#Q8
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

#A
Set4=Set1^Set2
print("8a) \n",Set4)

#B
Set5=Set1^(Set2^Set3)
print("8b) \n",Set5)

#c
Set6=(Set1&Set2)|(Set2&Set3)|(Set3&Set1)
print("8c) \n",Set6)

#D
newSet={1,2,3,4,5,6,7,8,9,10}
Set7=newSet-Set1
print("8d) \n",Set7)
#E
Set8=newSet-(Set1|Set2|Set3)
print("8e) \n",Set8)
