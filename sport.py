#TODO: import other classes
# from .group import *
# from .exception import *
from member import *
# from .dev import *

# class SportsNode:
#     def __init__(self,key):
#         self.key = key
#         self.memberdata = []
#         self.groupdata = []   

class Sports():
    def __init__(self,key=None):
        self.key = key
        self.size = 0
        self.sportsdict = {}
        self.m = Member()

    def __str__(self):

        newstr = ""
        print("\nThis is the current list of sports:")
        for key,values in self.sportsdict.items():
            newstr += "\n"+str(key)

        return newstr + f"\nNr of sports currently in the database are {self.size}"

    #FINISHED time complexity O(1)
    def register_sport(self):
        '''Adds a name to sports'''

        sportname = input("Enter the sportname to be added: ")

        new_sport = Sports(sportname)

        if sportname not in self.sportsdict:
            self.sportsdict[sportname] = {}
            print(f"{sportname} has been added. ")
            self.size += 1
        else:
            print("Sport already in database")
            return


    #FINISHED time complexity O(1)
    def remove_sport(self):
        '''Removes a given sport from the database'''
        
        sportname = input("What would you like to delete: ")

        if sportname in self.sportsarr:
            del self.sportsarr[sportname]
            print(f"{sportname} has been removed\n")
        else:
            print(f"{sportname} doesn't exists in database")


    #TODO: implement
    def remove_member_from_sport(self):
        '''Removes a member from a sport'''
        print("TO BE IMPLEMENTED")
        pass

        name_to_remove = input("Please enter the name to remove: ")
        sportremoved = input("Please enter the sport to remove from: ")


    def sign_for_sport(self):
        print("TO BE IMPLEMENTED")
        print("Member þarf að vera til og það þarf að vera hægt að leita af honum")
        membername = input("Who do you want to sign up for a sport: ")
        # realmember = find_member(member)
        sport = input("To which sport: \n")
        membername = input("Which member")
        self.m.find_member(membername)
        print("----------------------------------------")


        for key,values in self.sportsdict.items():
            if key == sport:
                self.sportsarr[key] = Member

        print("LOKIN")

    def find_in_sports(self):
        
        key = input("Which member would you like to find")
        for key,values in self.sportsdict.items():
            print(key,values)



    def __len__(self):
        return self.size
    
   
        






