def show_messages(messages):
    print("Showing All Messages.")
    for message in messages:
        print(message)
        
def send_messages(messages,sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)
        
messages = ['Hello','Hi Khushi','What!?','Why??','OKK']
show_messages(messages)

sent_messages = []
send_messages(messages,sent_messages)

print("\n")
print(messages)
print(sent_messages)