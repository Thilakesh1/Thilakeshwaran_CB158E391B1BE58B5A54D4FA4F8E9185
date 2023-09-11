class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, CGPA: {self.cgpa}"

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:
students = [
    Student("Alice", "001", 3.9),
    Student("Bob", "002", 3.7),
    Student("Charlie", "003", 4.0),
    Student("David", "004", 3.8),
]

sorted_students = sort_students(students)

print("Sorted Students:")
for student in sorted_students:
    print(student)