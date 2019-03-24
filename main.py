from group import *
# from .exception import *
from sport import *
from member import *
# from .dev import *

FRONT = f"""



                ##########################################################################################
                #                           Verkefni 6 í gagnaskipan, notkun ...                         #
                # -------------------------------------------------------------------------------------- #
                #                          Atli Þór & Wentzel Copyright 2019 (c)                         #
                ##########################################################################################
               
                """

FRONT += "                   -----------------VERY NICE TO SEE YOU-----------------\n\n"


class SportDatabase():
    def __init__(self):
        print(FRONT)
        print()
        self.s = Sports()
        self.m = Member()
        self.g = Group()

    def options(self):
        print()
        print("----NEW ITEMS----")
        print("[1] REGISTER NEW SPORT")
        print("[2] REGISTER A GROUP")
        print("[3] REGISTER NEW MEMBER")
        print("[4] SIGN MEMBER UP FOR A SPORT\n")
        print("----REMOVING ITEMS----")
        print("[5] REMOVE MEMBER FROM A SPORT")
        print("[6] REMOVE A SPORT FROM THE SYSTEM \n")
        print("----RETRIEVE DATA----")
        print("[7] LIST OF MEMBERS, PICK IN WHICH ORDER")  # order by name, age or sport
        print("[8] FIND A MEMBER")  # name, phone, email, age
        print("[9] SELECT A MEMBER AND GET ALL INFO, INCLUDING SPORTS")
        print("[10] SEE A LIST OF ALL SPORTS")
        print("[11] SELECT A SPORT AND SEE LIST OF USERS IN THAT SPORT")
        print()


    def do_again(self):
        '''Offers the user to do again or quit after each action'''

        x = input("You want to continue [Y/n]: ").upper()
        if x == "N":
            quit()
        elif x == "Y":
            self.main()
        else:
            print(f"{x} is not valid. Try again. ")
            self.do_again()


    def validate_input(self, option):
        '''Validates if input is an integer'''

        try:
            int(option)
            return option
        except ValueError:
            print("Input should be an integer")
            self.do_again()


    def main(self):
        self.options()
        option = str(input("ENTER YOUR CHOICE: \n"))
        option = self.validate_input(option)
        if option in "1,3,4,5,6,7,8,9,10,11":
            if option == "1":
                self.s.register_sport()
                self.do_again()

            elif option == "2":
                #TODO: Wentzel implementar
                pass

            elif option == "3":
                self.m.register_member()
                self.do_again()

            elif option == "4":
                #TODO implement
                self.s.sign_for_sport() #spurning hvort þetta ætti að vera s eða m
                self.do_again()

            elif option == "5":
                #TODO: implement
                self.s.remove_member_from_sport() #spurning hvort þetta ætti að vera s eða m
                self.do_again()

            elif option == "6":
                self.s.remove_sport() 
                self.do_again()

            elif option == "7":
                #TODO: implement sorting by sports
                self.m.get_ordered_list() #komið með aldur og nafn
                self.do_again()

            elif option == "8":
                #temp
                self.m.find_member()

            elif option == "9":
                pass

            elif option == "10":
                print(self.s)
                self.do_again()

            elif option == "11":
                pass

            else:
                print("Invalid number man!")
                self.do_again()

        self.main()
