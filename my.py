#print("Hello World...!!")
#print("*" * 10)
from ctypes import pythonapi

Student_count = 1000
rating = 4.99
is_published = True
course_name = 'python programming'
#print(course_name)
#print(len(course_name))
#print(course_name[0])
#print(course_name[-1])
#print(course_name[0:3])
#print(course_name[0:])
#print(course_name[:5])
#print(course_name[:])
course1 = "python \"programming"
course2 = "python \'programming"
course3 = "python \\programming"
course4 = "python \nprogramming"
#print(course1)
#print(course2)
#print(course3)
#print(course4)
first = "Kajal"
last = "Kumari"
full = first + " " + last
#print(full)
full2 = f"{first} {last}"
#print(full2)
full3 = f"{len(first)} {2+2}"
#print(full3)
course = "Python"
#print(course.lower())
#print(course.title())
#print(course.strip())
#print(10//3)
#print(10%3)
#print(10**3)
#X = input("x: ")
#y = int(X)+ 1
#print(f"X: {X}, y: {y}")
# int(X)
#float(X
#bool(X)
#str(X)

temp=15
if temp>30:
    print("It's warm")
    print("Drink water")
elif temp>20:
    print("It's nice")
else:
    print("It's cold")
#print("Done")
if 10=="10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

for number in range(1 , 10, 3):
    print("Attempt", number, number * ".")