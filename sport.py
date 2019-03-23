# Registration system for sports club
# The assignment is to program a system for registering data about sports, groups and members
# in a sports club. There is no particular API or class description to fill in and no part of the tests
# will be automated. The assignments will be evaluated based on functionality that works through
# the user interface. Code will be evaluated based on organization of classes and operations and
# what data structures are used. Operations that do not work in the user interface will not be
# evaluated for partial points based on code. User interfaces are evaluated based on efficiency
# and clarity of information, not on beauty. Text-based UI is sufficient.
# Base functionality - 50%


# ● User shall be able to register new sport
# ○ Name of sport
# ● User shall be able to register new member
# ○ Name
# ○ Phone
# ○ Email
# ○ Year of birth
# ● User shall be able to sign member up for a particular sport
# ● User shall be able to remove member from a sport
# ● User shall be able to remove a member from the system
# ● User shall be able to remove a sport from the system
# ● User shall be able to see a list of all members and order it on different data
# ○ Ordered by name
# ○ Ordered by age
# ○ Ordered by sport
# ● User shall be able to retrieve members by different data
# ○ Get by name
# ○ Get by phone
# ○ Get by email
# ○ Get by age or year of birth
# ● User shall be able to select a member and see detailed information about them
# ○ Name, phone, email, year of birth
# ○ All sports this user is registered in
# ● User shall be able to see a list of sports
# ● User shall be able to select a sport and see detailed information
# ○ List of users in the sport
# Operation memory and undo - 10%
# ● The system shall keep track of every operation done in the system
# ○ At least operations that change data
# ● The user shall be able to undo the last operation
# ○ Then the next-to-last, etc… like undo usually works
# Groups in sports - 10%
# ● User shall be able to register groups in each sport
# ○ Group name
# ○ Age from
# ○ Age to
# ● When signing a user up for a sport a group must be selected
# ○ Only groups for correct age available
# ○ Possible to sign into more than one group, if age allows
# ● When viewing details for a sport the user should see a list of groups
# ● User should be able to select a group and see details
# ○ List of users in a group
# ● When viewing details on a user the sport and group should be displayed in list
# Waiting lists - 10%
# ● The user shall be able to register a maximum number of members in a group
# ● If a group is full a member is added to waiting list instead
# ● If member is removed from a full group a member from the waiting list is added instead
# ○ Notify the user when this happens
# Persistent data - 10%
# ● The system shall store all data in files
# ○ Store when system is closed
# ■ prompt?
# ○ Store when user chooses to save
# ● The system shall read everything from the files when the system starts
# ○ Read data into more efficient data structures in memory
# Efficient data structures - 10%
# ● Efficient data structures should be used for each function of the system
# ○ Not everything in lists that are then sorted over and over
# ■ Use sorted structures when needed
# ■ Use multi-key structures where applicable
# ● But not when not needed
# ○ Use simple structures like stack and queue when sufficient
# Efficient flow of operations - 10%
# ● Make your system pleasant to use :)
# ○ Quick selections
# ■ Have numbered lines rather than having to enter full strings
# ○ Clear user interface
# ■ Windowed UI not required
# ● Operation can still be made clear and obvious

import datetime

NOW = datetime.datetime.now().year

WELCOME = "HELLO THERE. VERY NICE TO SEE YOU. WHAT WOULD YOU LIKE TO DO\n\n\n\n"
WELCOME += "PLEASE PICK YOUR OPTION: "

OPTIONS = "   SIGN member up\n   Remove a member from a sport \n   Remove a sport from the system \n  [7] See a list of all members\n".upper()

class InvalidInputException(Exception):
    pass


class MemberNode:
    def __init__(self,name:str,phone:str,email:str,birthyear:int,next=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.birthyear = birthyear #2000
        self.age = NOW - birthyear
        self.next = next

class GroupNode:
    def __init__(self,name:str,agefrom:int,ageto:int):
        self.name = name
        self.agefrom = agefrom
        self.ageto = ageto


class SportsNode:
    def __init__(self,key):
        self.key = key
        # self.userdata = 
        # self.groupdata = groupdata

    # def add(self,sportname):
        

class Sports:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.sportsarr = {}
# SportsNode() for i in range(self.capacity)

    def __len__(self):
        return self.size


    def find(self,key):

        if self.size == 0:
            return "NOT HERE"

        for key,value in self.sportsarr.items():
            print(key)

        
    # def __contains__(self,key):
    #     return self.find(key)
        


    def register_sport(self,sportname):
        '''Adds a name to sports'''

        index = hash(sportname)%self.capacity
        new_sport = SportsNode(sportname)

        # if sportname in Sports:
        #     return "EKKI HÆGT AÐ SKRÁ. ÍÞRÓTT ÞEGAR TIL"

        self.sportsarr[index] = new_sport
        self.size += 1

    
    def __str__(self):
        newstr = ""

        for key,value in self.sportsarr.items():
            newstr += str(key) + " "

        return newstr
        
class Group:
    def __init__(self,name:str,agefrom:int,ageto:int):
        self.name = name
        self.agefrom = agefrom
        self.ageto = ageto

class Member:
    def __init__(self,name:str,phone:str,email:str,birthyear:str):
        self.name = name
        self.phone = phone
        self.email  = email
        self.birthyear = birthyear


def Show_options():
    print("[1] REGISTER NEW SPORT")
    print("[2] REGISTER NEW MEMBER")
    print("[3] REGISTER NEW SPORT\n")
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



# ● User shall be able to sign member up for a particular sport
# ● User shall be able to remove member from a sport
# ● User shall be able to remove a member from the system
# ● User shall be able to remove a sport from the system
# ● User shall be able to see a list of all members and order it on different data
# ○ Ordered by name
# ○ Ordered by age
# ○ Ordered by sport