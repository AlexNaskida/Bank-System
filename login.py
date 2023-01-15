users = {
    'Jack' : 'password',
    'Luke' : '12345',
    'Jahn' : 'paroli',

}

def login():
    username = str(input('Enter your name: '))
    if username in users.keys():
        password = str(input(f'Enter password for {username}: '))
        if password == users[username]:
            print('Successfully logged in')
            print(f'Welcome {username}')
            return True, username

    print('Authentication failed')
    return (False,)


