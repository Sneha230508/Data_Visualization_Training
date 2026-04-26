# Program 6: Create and print dictionary

student = {
    "name": "Sneha",
    "age": 22,
    "course": "MCA"
}

print("Student Details:")
for key, value in student.items():
    print(key, ":", value)
    #Output
    """Student Details:
name : Sneha
age : 22
course : MCA"""