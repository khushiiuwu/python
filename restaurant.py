class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves wonderful {self.cuisine_type}")
        
    def open_restaurant(self):
        open = f"{self.restaurant_name} is open come and visit!"
        print(open)

restaurant = Restaurant("Stellar","Thai Cuisine")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaura = Restaurant("Honest","Indian Cuisine")
aura = Restaurant("Kesar","Indian Cuisine")
restaura.describe_restaurant()
aura.describe_restaurant()