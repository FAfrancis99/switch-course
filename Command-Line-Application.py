def palindrome_check(s):
    return s == s[::-1]


def lowercase_check(s):
    for ch in s:
        if not ('a' <= ch <= 'z'):
            return False
        return True


def digit_check(s):
    for ch in s:
        if not ('0' <= ch <= '9'):
            return False
        return True


def length_check(s,length = 15):
    return len(s) > length


def empty_check(s):
    return s == ""


def exit_program():
    print("Exit successfully")
    exit()


def show_operations():
    print("\nThe available operations are:")
    print("1 - Palindrome: Check if the input is palindrome")
    print("2 - Lower: Check if all characters in the input are lowercase")
    print("3 - Digit: Check if all characters in the input are digits")
    print("4 - Long: Check if the input length is longer than 15")
    print("5 - Empty: Check if the input is empty")
    print("6 - Exit: Exit successfully from the application")


def handle_input(check_func):
    user_input = input("Enter an input: ")
    result = check_func(user_input)
    print("The answer is: " + str(result))


def main():
    operations = {
        '1': lambda: handle_input(palindrome_check),
        '2': lambda: handle_input(lowercase_check),
        '3': lambda: handle_input(digit_check),
        '4': lambda: handle_input(length_check),
        '5': lambda: handle_input(empty_check),
        '6': exit_program
    }
    while 1:
        show_operations()
        choice = input("\nPlease enter the number of the operation you choose: ")
        if choice in operations:
            operations[choice]()
        else:
            print("the selected operation is not valid. please choose a number between 1-6.")


if __name__ == "__main__":
    main()
