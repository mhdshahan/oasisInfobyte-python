print("BMI Calculator")

#Take input from user
height = float(input("Enter your height:"))
weight = float(input("Enter your weight:"))

#Formula for BMI Calculation
bmi = weight/(height**2)

#Define a string
bmi_interpret = ""
if bmi <18.5:
    bmi_interpret="Underweight"
elif 18.5 <=bmi <24.9:
    bmi_interpret="normal"
elif 24.9<= bmi <29.9:
    bmi_interpret="Overweight"
else:
    bmi_interpret="obese"
#Display
print(f"BMI is :{bmi:.2f}")
print("BMI interpretation:",bmi_interpret)
