ages = "Enter a particular age."
while True:
    age = input(ages)
    if age == 'quit':
        break
    age = int(age)
    
    if age <=3:
        print("The ticket is free.")
    elif age>3 and age<=12:
        print("The ticket is $10")
    else:
        print("The ticket is $15")
    