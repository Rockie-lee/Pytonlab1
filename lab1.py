import math

# 1. Radius of a Circle
circumference = 5
radius_circle = circumference / (2 * math.pi)
print(f"Radius of the circle: {radius_circle:.2f}")

# 2. Volume of a Sphere
radius_sphere = 3
volume_sphere = (4/3) * math.pi * radius_sphere ** 3
print(f"volume of the sphere: {volume_sphere:.2f}")

# 3. Hypotenuse of a right Triangle
side_a = 3
side_b = 4
hypotenuse = math.sqrt(side_a ** 2 + side_b ** 2)
print(f"Hypotenuse of right Triangle: {hypotenuse:.2f} ")

# 4. String Manipulation
len('upper(Rockie)' + 'lower(Lee)')

# 5. BMI
age = 20
height_feet = 5.11
weight_lbs = 213

print("Data type of age", type(age))
print("Data type of height", type(height_feet))
print("Data type of weight", type(weight_lbs))

height_inches = height_feet * 12

BMI = (weight_lbs / (height_inches ** 2)) * 703
print(f"your BMI is: {BMI:.2f}")

