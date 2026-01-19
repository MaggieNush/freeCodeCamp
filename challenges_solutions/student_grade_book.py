def add_student(gradebook, student_info): 
    name = student_info[0].lower()
    grade = student_info[1]

    if name in gradebook:
        return "Student '{name}' already exists!"
    else:
        gradebook[name] = grade
        return f"Student '{name}' added with grade {grade}!"
    
def update_grade(gradebook, student_info):
    name = student_info[0].lower()
    grade = student_info[1]

    if name in gradebook:
        gradebook[name] = grade
        return f"Student '{name}' grade updated to {grade}!"
    else:
        return f"Student '{name}' does not exist!"
    
def remove_student(gradebook, name):
    name = name.lower()

    if name in gradebook:
        del gradebook[name]
        return f"Student '{name}' removed successfully!"
    else:
        return f"Student '{name}' not found!"

def view_gradebook(gradebook):
    if not gradebook:
        return "No students in gradebook."
    
    result = "Gradebook:\n"
    for name, grade in gradebook.items():
        result += f"{name.capitalize()}: {grade} "
    return result
    
# Testing codes & logic
gradebook = {}

print(add_student(gradebook, ("John", 85)))
print(add_student(gradebook, ("Mark", 90))) 
print(add_student(gradebook, ("Wendy", 95)))
print(update_grade(gradebook, ("Mark", 60)))
print(view_gradebook(gradebook))
