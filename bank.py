from login import login
from money import money



def main():
    while True:
        res = login()
        if res[0]:
            break
    money(res[1])



if __name__ == '__main__':
    main()