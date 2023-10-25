inp = "\n What topping     would you like on your pizza?"
inp += "\n Enter 'quit' when you are finished."

while True:
    toppings = input(inp)
    if toppings != 'quit':
        print(f"I'll add {toppings} to your pizza.")
    else:
        break