def login(users):
    username = str(input('Enter your name: '))
    if username in users.keys():
        password = str(input(f'Enter password for {username}: '))
        if password == users[username]:
            print('Successfully logged in')
        else:
            print('Invalid password')
    else
        print('Invalid username')