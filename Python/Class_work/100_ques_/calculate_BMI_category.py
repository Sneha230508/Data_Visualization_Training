# Program to calculate BMI

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)

print("BMI =", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
#Output
"""Enter weight in kg: 50
Enter height in meters: 152
BMI = 0.002164127423822715
Underweight"""