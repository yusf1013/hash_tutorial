import random, bcrypt
import time
from itertools import permutations

credentials = {}
salt = bcrypt.gensalt()


def generate(starting_str, length):
    ans = []
    perms = permutations(starting_str, length)
    for k in list(perms):
        item = ""
        for x in k:
            item += x
        ans.append(item)

    return ans


def main():
    while True:
        choice = input("1. Login\n2. Register\n3. Bruteforce\n")
        if choice == "1":
            username = input("username: ")
            password = input("password: ")
            if username not in credentials:
                print("User does not exist")
            elif bcrypt.checkpw(bytes(password, encoding='utf-8'), credentials[username]):
                print("success")
            else:
                print("failed")
        elif choice == "2":
            username = input("username: ")
            password = input("password: ")
            # pepper = random.choice(search_str)
            # print(pepper)
            # hashed = bcrypt.hashpw(bytes(password, encoding='utf-8'), s)
            # credentials[username] = hash(password+salt+pepper)
            credentials[username] = bcrypt.hashpw(bytes(password, encoding='utf-8'), salt)
        elif choice == "3":
            username = input("enter victim's username: ")
            p1 = generate("0123456789", 2)
            # p1 = generate("abcdefghijklmnopqrstuvwxyz", 4)
            # p1 = generate("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3)
            start = time.time()
            for password in p1:
                if username not in credentials:
                    print("User does not exist")
                elif bcrypt.checkpw(bytes(password, encoding='utf-8'), credentials[username]):
                    print("success", password)
                    end = time.time()
                    print(end - start)
                    break
                else:
                    print("failed", password)
        else:
            print("error")

        print(credentials)


main()
