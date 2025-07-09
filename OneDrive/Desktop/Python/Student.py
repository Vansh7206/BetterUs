print("Hello  this is Somaiya college marksheet")
name = "Vansh Chandan"
rollno = "31011224007"
course = "SYBCA"

print("Name of student is:",name)
print("Roll No. is:",rollno)
print("Course chosen is:",course)

print("PLease Enter your marks of DBMS below")
DBMS = float(input())
print("Enter the marks of Python")
Python = float(input())
print("Enter the marks of Statistic")
Stats = float(input())
print("Enter the marks of OS")
OS = float(input())

Total = DBMS + Python + Stats + OS
Total2 = Total/4
print(Total2)

if(Total2>=90):
    print("A")
elif(Total2>=80):
    print("B")
elif(Total2>=70):
    print("C")
else:
    print("Fail")


