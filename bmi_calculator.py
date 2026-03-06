# BMI Calculator with Status Classification

# Taking user input
name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# BMI calculation
bmi = weight / (height ** 2)

# BMI classification
if bmi < 18.5 :
     status = "Under Weight"
elif bmi >=18.5 and bmi<=24.9:
     status = "Normal"
elif bmi >=25 and bmi <=29.9:
     status = "Over Weight"
else:
     status = "Obesity"

# Output message
print(f"\nDear {name}!!!")
print("Welcome to Guvi Fitness Center!")
print(f"Your BMI is {bmi} and your BMI Status is {status}")




