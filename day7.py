#  how to use an array 

arr = [0, 1, 2, 3, 4, 5]

print(f"You can print these all by calling its variable name {arr}")

# but also you can specify the value you are trying to call
# also the sample i create is the way on how indexing work where it start from 0 and so on

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])
print(arr[5])

# you can put anything in the array like string, integer and float

values = ["Ak-47", 32, 12.00, "My N****", 0.300000000004]
print(f"Value 1 :  {values[0]}, Value 2: {values[1]}, Value 3: {values[2]}, Values 4: {values[3]}")


#  also you can insert a new value in array using append
input_something = input("Enter a value which will store in the array: ")
storage = ["Alice Guo","Carlos","Sarah Duterte","Ang Kaibigan", "Meow meow meow"]
storage.append(input_something)
print(storage)