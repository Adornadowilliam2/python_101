#  write a program to find the area of  a triangle

#  Input the base and height from the user
base = float(input("Enter the length of the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))


#calculate the area of the triangle
area = 0.5 * base * height

# Display the result
# by using f in the first you can insert the value in the string
# like in such same idea in the Php programming language
# to print a value we use ${value}
#  here in python you can simply just add f in the first line before the double quote string
print(f"The area of the triangle us: {area}")

# Try to make a converter the turn height into centimeter