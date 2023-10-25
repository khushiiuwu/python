def sandwich(*items):
    print("\n I'll make your sandwich.")
    
    for item in items:
        print(f"I'll add {item} to your sanwich!")
    print("Your sandwich is ready")
sandwich('Cheese')
sandwich('Tomato','Onion','Mayo')
sandwich('Onion','Potato','Ketchup')
