import random
# Initialize an empty list to store students as dictionaries
student_list = []
index =1
# Function to display menu
def display_menu():
    print("\nstudent Management System")
    print("1. Display students")
    print("2. Add student")
    print("3. Set student Size")
    print("4. Group students by Size")
    print("5. Exit")

# Function to display all students
def display_students():
    
    if not student_list:
        print("No students added yet.")
    else:
        for i, student in enumerate(student_list):
            print(f"{i + 1}. student: {student['name']}, Size: {student['size']}")
            
            for name in student['list_of_group']:
             print(f' {random_index()} {(name).capitalize()}')
            

def random_index(): 
    if len(student_list)>1:
      index = random.randint(1, len(student_list)-1)
      return index
    else:
     return random.randint(1, 1000)


# Function to add a new student
def add_student():
    name = input("Enter the name of the student group: ")
    list_of_student=input(f'list of student in the group').split()
    size = input("Enter the size of the student (small, medium, large): ")
    new_student = {'name': name, 'size': size, 'list_of_group':list_of_student}
    student_list.append(new_student)
    print(f"{name} added.")

# Function to set size for an existing student
def set_student_size():
    display_students()
    index = int(input("Select the number of the student to update its size: ")) - 1
    if 0 <= index < len(student_list):
        new_size = input("Enter the new size (small, medium, large): ")
        student_list[index]['size'] = new_size
        print(f"{student_list[index]['name']}'s size updated to {new_size}.")
    else:
        print("Invalid selection.")

# Function to group students by size
def group_students_by_size():
    small_students = [student for student in student_list if student['size'] == 'small']
    medium_students = [student for student in student_list if student['size'] == 'medium']
    large_students = [student for student in student_list if student['size'] == 'large']
    
    print("\nGrouped students by Size:")
    
    print("\nSmall students:")
    if small_students:
        for student in small_students:
            print(f"student: {student['name']}, Size: {student['size']}")
            for name in student['list_of_group']:
             print(f' {random_index()} {(name).capitalize()}')
    else:
        print("None")
    
    print("\nMedium students:")
    if medium_students:
        for student in medium_students:
            print(f"student: {student['name']}, Size: {student['size']}")
            for name in student['list_of_group']:
             print(f' {random_index()} {(name).capitalize()}')
    else:
        print("None")
    
    print("\nLarge students:")
    if large_students:
        for student in large_students:
            print(f"student: {student['name']}, Size: {student['size']}")
            for name in student['list_of_group']:
             print(f' {random_index()} {(name).capitalize()}')
    else:
        print("None")

# Main program loop
while True:
    display_menu()
    choice = input("\nEnter your choice: ")

    if choice == '1':
        display_students()
    elif choice == '2':
        add_student()
    elif choice == '3':
        set_student_size()
    elif choice == '4':
        group_students_by_size()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
