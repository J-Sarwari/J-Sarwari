# Get the user's height and weight
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate the BMI
bmi = weight / (height ** 2)

# Determine the weight category
if bmi < 18.5:
    weight_category = "Underweight"
elif bmi < 25:
    weight_category = "Normal weight"
elif bmi < 30:
    weight_category = "Overweight"
else:
    weight_category = "Obese, please consult a doctor"

# Display the results
print(f"Your BMI is: \[{bmi:.2f}\]")
print(f"Your weight category is: {weight_category}")