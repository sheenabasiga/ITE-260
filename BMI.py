

def getBMI (x,y):
    return x/y

def display_category(x):
    if x < 16.5:
        return first_condition
    elif x <= 18.4:
        return second_condition
    elif x <= 24.9:
        return third_condition
    elif x <= 30:
        return fourth_condition
    elif x <= 34.9:
        return fifth_condition
    elif x <= 40:
        return sixth_condition
    else:
        return seventh_condition

# Code to input the user's details
weight = int(input("Enter your weight in kilograms: "))
height = int(input("Enter your height in meters: "))
height_squared = height**2

#Initialize the user's condition
first_condition = "Severly Underweight"
second_condition = "Underweight"
third_condition = "Normal"
fourth_condition = "Overweight"
fifth_condition = "Obese Class 1"
sixth_condition = "Obese Class 2"
seventh_condition = "Obese Class 3"

#Compute for the output
BMI = getBMI(weight, height_squared)
category = display_category(BMI)

#Print the Output
print (BMI)
print("Your BMI is", BMI, "You are", category)
