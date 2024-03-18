# https://www.codewars.com/kata/55ddcef532f8678af1000006

class ReNameAbleClass(object):
    @classmethod
    def change_class_name(cls, new_name: str):
        if not (new_name[0].isupper() & new_name.isalnum()):
            raise Exception("Invalid")
        cls.__name__ = new_name
        
    @classmethod
    def __str__(cls):
        return f"Class name is: {cls.__name__}"