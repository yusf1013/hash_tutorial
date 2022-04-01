import random

credentials = {}
salt = "adsf"
search_str = "abcdefghijklmnopqrstuvwxyz"


def hash(in_str):
    sum = 0
    for char in in_str:
        sum += search_str.find(char) + 1

    return sum


def match_password(password_input, hash_value):
    for char in search_str:
        if hash_value == hash(password_input+salt+char):
            return True

    return False


def main():
    while True:
        choice = input("1. Login\n2. Register\n")
        if choice == "1":
            username = input("username: ")
            password = input("password: ")
            if username not in credentials:
                print("User does not exist")
            elif match_password(password, credentials[username]):
                print("success")
            else:
                print("failed")
        elif choice == "2":
            username = input("username: ")
            password = input("password: ")
            pepper = random.choice(search_str)
            print(pepper)
            credentials[username] = hash(password+salt+pepper)
        else:
            print("error")

        print(credentials)


main()
