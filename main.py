# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
int_weight = int(weight)
float_height = float(height)
bmi = int_weight / float_height**2
rounded_bmi = round(bmi)
print(rounded_bmi)
