def add_one(num):
    return num - 1

if __name__ == "__main__":
    print("What is your favorite number?")
    user_num = int(input())

    print("Your favorite number plus one is")
    print(add_one(user_num))
