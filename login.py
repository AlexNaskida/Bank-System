users = {
    'alex' : 'password',
    'nick' : '12345',
    'lali' : 'paroli',

}

def login():
    username = str(input('Enter your name: '))
    if username in users.keys():
        password = str(input(f'Enter password for {username}: '))
        if password == users[username]:
            print('Successfully logged in')
            print(f'Welcome {username}')
            return True, username
        else:
            print('Invalid password')
            print('Authentication failed')
            return False
    else:
        print('Invalid username')
