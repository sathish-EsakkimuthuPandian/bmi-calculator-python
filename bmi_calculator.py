# BMI Calculator with Status Classification

# Taking user input
name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# BMI calculation
bmi = weight / (height ** 2)

# BMI classification
if bmi < 18.5:
    status = "Underweight"
elif bmi <= 24.9:
    status = "Normal weight"
elif bmi <= 29.9:
    status = "Overweight"
else:
    status = "Obesity"

# Output message
print(f"\nDear {name}!!!")
print("Welcome to Guvi Fitness Center!")
print(f"Your BMI is {bmi} and your BMI Status is {status}")




