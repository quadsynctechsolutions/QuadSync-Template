class Student:
    """Represents a single student as an object."""
    def __init__(self, roll_no, name, age, grade):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.grade = grade
        
    def display(self):
        print(f"Roll No: {self.roll_no} | Name: {self.name} | "
        f"Age: {self.age} | Grade: {self.grade}")
        
        
class StudentManagementSystem:
    """A simple menu-driven Student Management System."""
    def __init__(self):
        # Dictionary to store Student objects: {roll_no: Student object}
        self.students = {}
        
    def add_student(self):
        roll_no = input("Enter Roll Number: ").strip()
        if roll_no in self.students:
            print("A student with this roll number already exists!")
            return
        name = input("Enter Name: ").strip()
        age = input("Enter Age: ").strip()
        grade = input("Enter Grade/Class: ").strip()
        self.students[roll_no] = Student(roll_no, name, age, grade)
        print("Student added successfully!")
        
    def view_students(self):
        if not self.students:
            print("No student records found.")
            return
        print("\n--- Student Records ---")
        for student in self.students.values():
            student.display()

    def update_student(self):
        roll_no = input("Enter Roll Number to update: ").strip()
        if roll_no not in self.students:
            print("Student not found!")
            return
        print("Leave a field blank to keep its current value.")
        student = self.students[roll_no]
        name = input(f"New Name [{student.name}]: ").strip()
        age = input(f"New Age [{student.age}]: ").strip()
        grade = input(f"New Grade [{student.grade}]: ").strip()
        if name:
            student.name = name
        if age:
         student.age = age
        if grade:
         student.grade = grade
        print("Student record updated successfully!")
        
    def delete_student(self):
        roll_no = input("Enter Roll Number to delete: ").strip()
        if roll_no in self.students:
            del self.students[roll_no]
            print("Student deleted successfully!")
        else:
            print("Student not found!")
            
    def search_student(self):
        roll_no = input("Enter Roll Number to search: ").strip()
        if roll_no in self.students:
            self.students[roll_no].display()
        else:
            print("Student not found!")
            
    def menu(self):
        while True:
            print("\n===== Student Management System =====")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Search Student")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                self.search_student()
            elif choice == "6":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 6.")
                
                
system = StudentManagementSystem()
system.menu()