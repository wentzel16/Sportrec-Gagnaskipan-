# from .group import *
# from .exception import *
from sport import *
from member import *
# from .dev import *

import datetime
NOW = datetime.datetime.now().year

class Member:
    def __init__(self,ssn=None,name=None,phone=None,email=None,birthyear=None):
        self.ssn = ssn
        self.name = name
        self.phone = phone
        self.email  = email
        self.birthyear = birthyear
        if birthyear:
            self.age = NOW - int(birthyear)
        self.memberarr = {}
        self.size = 0
        # self.arr = Sports()
    

    # def verify_input(self,birthyear):

    #     if len(birthyear) == 4:
    #         return birthyear
    #     else:
    #         print("You can´t be born that year.")

        #     birthyear = int(birthyear)
        #     return NOW - int(birthyear)
        # except ValueError:
        #     print("Birthyear has to be an integer")


    #FINISHED O(1)
    def register_member(self):
        '''Registers a member to the system'''

        ssn = input("Please enter your SSN: ")
        name = input("Please enter your name: ")
        phone = input("Please enter your phone: ")
        email = input("Please enter your email: ")
        yearofbirth = input("Please enter your year of birth: ")
        if name and phone and email and yearofbirth and ssn:
            new_member = Member(ssn,name,phone,email,yearofbirth)
            self.memberarr[id] =new_member
            self.size += 1


    def get_ordered_list(self):

        print("Get your list of members....")
        print("[1] Ordered by name")
        print("[2] Ordered by age")
        print("[3] Ordered by sport")
        order = input()

        order = self._validate_input(order)

        if not order:
            return
        
        return self._print_order(order)


    def _validate_input(self,order):
        
        try:
            int(order)
            return str(order)
        except ValueError:
            print(f"{order} is not an option")


        

        # print(self.__str__())
        # print()
        # member = input("Whom are you looking for? ")


    def __lt__(self,other):
        return self.age < other.age
        # elif self.sport:
        #     return self.sport < other.sport


    def _print_order(self,order):

        if order == "1":
            print()
            print("Sorted by name......")    
            print(self.__str__())
        
        elif order =="2":
            print()
            print("Sorted by age......")
            for member in sorted(self.memberarr):
                print(f"ID: {str(member.id)}, Name:{str(member.name)}, Phone: {member.phone}, Email: {str(member.email)}, Age: {str(member.age)}")
        
        elif order == "3":
            print("NOT READY FOR THIS OPTION")
            print()
            quit()

     #TODO: implement
    
    
    def find_member(self):
        print("atliatliatliatli")
    




    def __len__(self):
        return self.size


    def __str__(self):

        ret_str = ""

        for member in self.memberarr:
            ret_str += f"ID: {str(member.ssn)}, Name: {str(member.name)}, Phone: {member.phone}, Email: {str(member.email)}, Age: {str(member.age)}\n"

        return ret_str.strip()
        

 