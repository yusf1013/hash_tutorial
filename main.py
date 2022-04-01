credentials = {}

def hash(in_str):
    search_str = "abcdefghijklmnopqrstuvwxyz"
    sum = 0
    for char in in_str:
        sum += search_str.find(char) + 1

    return sum


def main():
    while True:
        choice = input("1. Login\n2. Register\n")
        if choice == "1":
            username = input("username: ")
            password = input("password: ")
            if username not in credentials:
                print("User does not exist")
            elif credentials[username] == hash(password):
                print("success")
            else:
                print("failed")
        elif choice == "2":
            username = input("username: ")
            password = input("password: ")
            credentials[username] = hash(password)
        else:
            print("error")

        print(credentials)


main()
