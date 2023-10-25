#Use a variable to represent a person's name, and print a message to that person. Your message should be simple, such as,
#"Hello Eric, would you like to learn some Python today?"
name = "Khushi"
print(f"Hello {name}, would you like to learn some python today? ")
#Find a quote from a famous person you admire. Print thequote and the name of its author. Your output should look something like the
#following, including the quotation marks:
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')
famous_name = "Albert Einstein"
message = "A person who never made a mistake never tried anything new."
print(f'\t{famous_name} once said,\n "{message}"'.lstrip())
print(f'\t{famous_name} once said,\n "{message}"'.rstrip())
print(f'\t{famous_name} once said,\n "{message}"'.strip())