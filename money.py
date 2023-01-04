
balance = {
    'alex' : 0,
    'nick' : 0,
    'lali' : 0,

}

def money(username):
    while True:
        process=input('Choose an operation you want to do (put, show, withdraw): ')
        if process == 'put':
            amount = int(input('Enter amount money you want to put: '))
            balance[username] += amount
            print(f'Done. Current amount {balance[username]}')
        elif process == 'show':
            print(f'Current amount {balance[username]}')
        elif process == 'withdraw':
            amount = int(input('Enter amount money you want to withdraw: '))
            if amount > balance[username]:
                print("You don't have enough money to withdraw. please enter lower amount")
            else:
                balance[username] -= amount
                print(f'Done. Current amount {balance[username]}')
        else:
            print('Invalid input')