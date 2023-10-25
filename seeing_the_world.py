places = ['Mauritius','Paris','London','Tokyo','Seoul']
print(places)
#Use sorted() to print your lsit in aplhabetical order without modifying the actual list
print(sorted(places))
#Showing that the actual list is still in the same order!
print(places)
#Using reverse to change the order of the list and printing it to show that its order has changed.
places.reverse()
print(places)
#Using the reverse() again to change the order of teh list to it's original form
places.reverse()
print(places)
#Using sort() to change the list  in an alphabetical order!
places.sort()
print(places)
#Using sort() to change the list to reverse alphabetical order.
places.sort(reverse=True)
print(places)