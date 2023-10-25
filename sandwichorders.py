sandwich_orders = ['veggie','cheesy','jalapeno','bombay']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
    
for finished in finished_sandwiches:
    print(f"I made your {finished} sandwich.")