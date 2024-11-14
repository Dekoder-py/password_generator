from password_gen import PasswordGen


def main():
    length = int(input("How long do you want the password: "))

    numbers_input = input("Do you want numbers in your password (yes/no): ")
    if numbers_input.lower() == "yes":
        numbers_bool = True
    else:
        numbers_bool = False
    print(PasswordGen(length, numbers_bool).gen())


main()
