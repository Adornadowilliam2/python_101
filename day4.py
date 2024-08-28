# learning using condition statement 
#  as you can see i use it in day3 even i did not explain what does do
#  the purpose of that is to have validation to avoid showing error
#  to use this just create an scenario

# Print Good morning if the user type morning else Good day

message = str(input("Enter a message: "))
gay = "means you're gay"
if message == "Good morning":
    print("Good morning!")
else:
    print("Good day!")
   
day_is_it = input("Enter the day today: ")
if day_is_it == "Monday":
    print("I dont like mondays")
elif day_is_it == "Tuesday":
    print("School work Tuesday")
elif day_is_it == "Wednesday":
    print(f"Wednesday {gay}") 
elif day_is_it == "Thursday":
    print("One day to go! Thursday")
elif day_is_it == "Friday":
    print("Finally a weekends rest tommorrow, Friday")
elif day_is_it == "Saturday":
    print("WHo said i have a rest day , Saturday")
elif day_is_it == "Sunday":
    print("Amen, Sunday")
else: 
    print("Error")