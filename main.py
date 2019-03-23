import datetime
from group import *
from exception import *
from sport import *


NOW = datetime.datetime.now().year
WELCOME = "HELLO THERE. VERY NICE TO SEE YOU. WHAT WOULD YOU LIKE TO DO\n\n\n\n"
WELCOME += "PLEASE PICK YOUR OPTION: "

OPTIONS = "   SIGN member up\n   Remove a member from a sport \n   Remove a sport from the system \n  [7] See a list of all members\n".upper()

def Show_options():
    print("[1] REGISTER NEW SPORT")
    print("[2] REGISTER NEW MEMBER")
    print("[3] SIGN MEMBER UP FOR A SPORT")
    print("[4] REMOVE MEMBER FROM A SPORT")
    print("[4] USER OPTIONS: \n")
    print(OPTIONS)


def do_again():
    x = input("Wanna try again [Y/n]").upper()
    if x == "N":
        quit()
    elif x == "Y":
        main()


def validate_input(option):

    try:
        int(option)
        return int(option)
    except ValueError:
        print("Input should be an integer")
        do_again()


s = Sports()

def main():
    print(WELCOME)
    print()
    Show_options()
    option = input("ENTER YOUR CHOICE: ")
    option = validate_input(option)
    if 0 < option <8:
        if option  == 1:
            name = input("Enter the sportname to be added: ")
            s.register_sport(name)
            main()

        elif option == 7:
            print("arara")
            print(s)
    else:
        print("Invalid number man!")
        do_again()

main()