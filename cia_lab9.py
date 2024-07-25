# Input is the string "password"

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter the password to encode: ")
            original = password
            password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == "2":
            print(f"The encoded password is {password}, and the original password is {original}.\n")
        elif option == "3":
            print("Thank you!")
            exit()
        else:
            print("Invalid option!")


def encode(password):
    new_password = []
    for char in password:
        char = int(char)
        if 0 <= char <= 6:
            char = str(char + 3)
        elif char == 7:
            char = "0"
        elif char == 8:
            char = "1"
        elif char == 9:
            char = "2"
        new_password.append(char)
    encoded_pw = ''.join(new_password)
    return encoded_pw


# decode function!
def decode(password):
    pass # to be completed by partner


if __name__ == "__main__":
    main()