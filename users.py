class User:
    def __init__(self, first_name, last_name,username,email,location,):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"Name {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"e-mail : {self.email}")
        print(f"Location: {self.location}") 
        
    def greet_user(self):
        print(f'Hello {self.username}!')
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
#creating an instance  for the class User
user = User("Khushi",'Patel','khukhu','khume3103@gmail.com','Vadodara')
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"login attempts: {user.login_attempts}")
user1 = User('Lamia',"Faria",'lamia','lami@gmail.com','Bangladesh')
user1.describe_user()

user2 = User('Janvi','Patel','janu','janvip@gmail.com','Vadodara')
user2.describe_user()