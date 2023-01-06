from history import history, log

balance = {
    'alex' : 0,
    'nick' : 0,
    'lali' : 0,
}

def money(username):
    while True:
        process=input('Choose an operation you want to do (put/p, show/s, withdraw/w, history/h): ')
        if process in ['p', 'put']:
            amount = int(input('Enter amount money you want to put: '))
            balance[username] += amount
            print(f'Done. Current amount {balance[username]}')
            log(username, f'+{amount}')
        elif process in ['show', 's']:
            print(f'Current amount {balance[username]}')
        elif process in ['history','h']:
            print(f'Your logs are {history[username]}')
        elif process in ['withdraw', 'w']:
            amount = int(input('Enter amount money you want to withdraw: '))
            if amount> balance[username]:
                print("You don't have enough money to withdraw. please enter lower amount")
            else:
                balance[username] -= amount
                print(f'Done. Current amount {balance[username]}')
                log(username, f'-{amount}')
        else:
            print('Invalid input')
