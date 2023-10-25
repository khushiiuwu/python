def max(a,b):
    if a > b:
        return a
    else:
        return b        
def min(a,b):
    if a > b:
        return b
    else:
        return a

   
a = int(input("Enter value of a"))
b = int(input("Enter value of b"))

print(max(a,b))
print(min(a,b))