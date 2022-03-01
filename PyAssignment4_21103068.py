#Q1
print("Q1")
def Towerofhanoi(n,initial,extra,final):
    if n==1:
        print ("Move disk 1 from rod",initial,"to rod",final)
        return
    Towerofhanoi(n-1,initial,final,extra)
    print("Move from ",initial," to ",final)
    Towerofhanoi(n-1,extra,initial,final)
        
Towerofhanoi(3,"A","B","C") #3 disks are used as given in the problem  
                          	#A is the initial rod
							#B is the extra rod 
							#C is the final rod 
print()

#Question 2
print("Q2")
n=int(input("Enter the number of rows: "))

#using recursion:
def pascalsTriangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        newRow = [1]
        result = pascalsTriangle(n-1) #recursive statement
        lastRow = result[-1]
        for i in range(len(lastRow)-1):
            newRow.append(lastRow[i] + lastRow[i+1])
        newRow += [1]
        result.append(newRow)
    return result

print("Recursion:")
for i in pascalsTriangle(n): #returns list of lists of rows of pascal's triangle
    for j in i:              
        print(j,end=' ') #required format
    print('')

#Using iteration
def factorial(n):  #defining factorial
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return factorial(n-1)*n

def C(n,r): #defining nCr 
    return int(factorial(n)/((factorial(n-r))*(factorial(r))))

print("Iteration: ")
i=0
while i<n:
    for j in range(0,i+1):
        print(C(i,j),end=' ') #required format
    print('')
    i+=1
    print()
    
#Q3
print("Q3")
def div(a,b): #Function to calculate quotient and remainder
    quo=a//b #Finds quotient
    rem=a%b #Finds remainder
    print("Quotient: ",quo)
    print("Remainder: ",rem)
    return quo,rem

a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
result=div(a,b) #calling of the above function
print(result)

print("3a)")
print("The function is callable: ",callable(div)) #callable() checks whether the function is callable or not
print()

print("3b)")
if a==0:
    print("a is zero")
if b==0:
    print("b is zero")
if result[0]==0:
    print("quotient is zero")
if result[1]==0:
    print("remainder is zero")
if a!=0 and b!=0 and result[0]!=0 and result[1]!=0: #The statement is true only when none of the parameters are zero
    print("Everything is non-zero")
print()

print("3c")
list_result=list(result) #list_result is a new list made from a tuple
add_val=[4,5,6] #given
newSet=list_result+add_val #addition of 2 lists
print(newSet)

extra=[] #empty list
for i in newSet: 
    if i>4:
        extra.append(i) #adds the i to extra-the list
print("Numbers greater than 4 are: ",extra)
print()

print("3d")
extraSet=set(extra) #new set made from a list
print(extraSet)
print()

print("3e)")
immSet=frozenset(extraSet) #new immutable frozen set made from an existing set
print(immSet," is now an immutable set")
print()

print("3f)")
max=0 #a helping parameter
for i in immSet:
    if i>max:
        max=i
print("The maximum value in the set is: ",max)
print("The hash value is: ",hash(max)) #gets the hash value of the maximum values
print()

#Q4
print("Q4")
class Student:
    def __init__(self,name,sid): #constructor
        self.name=name #records name
        self.sid=sid #records sid
    def __del__(self): #destructor
        print("The object is destroyed")

S1=Student("vanshaj",3068) #new object S1
print("Name: ",S1.name)
print("SID: ",S1.sid)
print()

#Q5
print("Q5")
class Employee: #creates new class
    def __init__(self,name,salary): #constructor
        self.name=name #records name
        self.salary=salary #records salary

E1=Employee("Mehak",40000)
E2=Employee("Ashok",50000)
E3=Employee("Viren",60000)

print("5a)")
E1.salary=70000 #salary changed
print("Updated Salary of Mehak: ",E1.salary)
print("5b)")
del E3 #deletes E3's records(name and salary)
print("Viren's record deleted.")
print()

#Q6
print("Q6")
def anagram(word):
    if len(word)==1:
        return [word]
    partial=anagram(word[1:])
    char=word[0]
    result=[]
    for perm in partial:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:])
        return result

george=input("Enter a word: ")
possible=anagram(george)
barbie=input("Enter another word: ")
print("The possible words are: ",possible)
if barbie in possible:
    print("The friendship is real")
else: 
    print("The friendship is fake")


