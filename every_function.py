languages = ['Gujarati','Hindi','English','German','French','Korean']
print(languages)

#Adding an element to the list using append() method.
languages.append('Spanish')
print(languages)

#Adding an element to the list using insert() method.
languages.insert(3, 'Marathi')
print(languages)

#Removing an item using del Statement
del languages[3]
print(languages)

#Removing an Item using pop() method
popped_languages = languages.pop()
print(popped_languages)
print(languages)

#Popping items from any position in a list
popped_language = languages.pop(1)
print(popped_language)
print(languages)

#Removing an Item by value using remove() method
languages.remove('Korean')
print(languages)

#Sorting a list permanently with sort() method
languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)

#Sorting a list temporarily with the sorted() function
print(sorted(languages))

#Printing a list in reverse order
languages.reverse()
print(languages)

#fidning length of the list
print(len(languages))