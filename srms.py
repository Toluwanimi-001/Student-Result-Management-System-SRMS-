# Student Result Management System

students = []

def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"

def add_student():
    name = input("Enter student name: ")
    s1 = float(input("Enter score for Subject 1: "))
    s2 = float(input("Enter score for Subject 2: "))
    s3 = float(input("Enter score for Subject 3: "))

    total = s1 + s2 + s3
    average = total / 3
    grade = calculate_grade(average)

    students.append({
        "name": name,
        "total": total,
        "average": average,
        "grade": grade
    })

def view_results():
    for student in students:
        print(student)

while True:
    print("\n1. Add Student Result")
    print("2. View Results")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_results()
    elif choice == "3":
        break
