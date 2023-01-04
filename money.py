
balance = {
    'alex' : 0,
    'nick' : 0,
    'lali' : 0,

}

def money(username):
    process=input('Choose an operation you want to do (put, show, withdraw): ')
    if process == 'put':
        amount = input('Enter amount money you want to put: ')
        balance[username] = amount
        print('Done')
    elif process == 'show':
        print(balance[username])
    else:
        amount = input('Enter amount money you want to withdraw: ')
        if amount > balance[username]:
            print("You don't have enough money to withdraw. please enter lower amount")
        else:
            print('Done')