class MemberNode:
    def __init__(self,name:str,phone:str,email:str,birthyear:int,next=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.birthyear = birthyear #2000
        self.age = NOW - birthyear
        self.next = next

class Member:
    def __init__(self,name:str,phone:str,email:str,birthyear:str):
        self.name = name
        self.phone = phone
        self.email  = email
        self.birthyear = birthyear