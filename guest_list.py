#If you could invite anyone, living or deceased, to dinner, who would you invite? Make  alist that includes at least three people you'd 
#like to invite dinner. Then use you list to print a message to each person, inviting them to dinner.
guests = ['Khushi','Shiv','Mom','Dad','Mauli','Shreeja','Uncle','Aunty']
for guest in guests:
    print(f"Hey {guest.title()}, you are invited to Khushi's dinner party!")
    
name = guests[5].title()
print(f"Sorry! {name} can't make it to the dinner party :(!" )

del(guests[5])
guests.insert(5,'Lia')
print(guests)     
print("There are total", len(guests), "guests")