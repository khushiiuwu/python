pizzas = ["Margaretha","Jalapeno","Tomato"]
friend_pizzas = pizzas[:]

pizzas.append('onion')
friend_pizzas.append('pepper')

print("My favourite pizza are:")
for pizza in pizzas:
    print(f"- {pizza}")
 
print("\n My friend's favourite pizzas are")   
for friend_pizza in friend_pizzas:
    print(f"- {friend_pizza}")