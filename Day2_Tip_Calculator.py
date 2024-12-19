print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15?  "))
no_of_people = int(input("How many people to split the bill?"))
Amount = bill * (1+ (tip_percent/100))
Per_person_contribution = Amount / no_of_people
print(f"Each person should pay: ${(round(Per_person_contribution,2))}")