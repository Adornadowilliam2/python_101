#  DO you finish the work don't go here if you still not do yet.
# addition 
num1 = float(input("Enter the first number for addition:"))
num2 = float(input("Enter the second number for addition:"))

sum_result = num1 +  num2
print("Total", sum_result)

#division
num1_value = float(input("Enter the dividend for division: "))
num2_value =  float(input("Enter the divisor for division: "))
if num2_value == 0:
    print("Error: Division by zero is zero so shutdup")
else:
    division_result = num1_value /  num2_value
    print("Quotient: ", division_result)
    
    
# now create a simple calculator with the use of if else