current_users = ['Khushi','Tisha','Janvi','Anisha','Neha']
current_user = [user.lower() for user in current_users]
new_users = ['Mauli','Dishita','Tani','Neha','Diya']

for new in new_users:
        if new.lower() in current_user:
            print(f"{new} will need to enter a new username.")
        else:
            print(f"{new} username is available")
            