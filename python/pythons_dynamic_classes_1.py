# https://www.codewars.com/kata/55ddb0ea5a133623b6000043

def class_name_changer(cls, new_name: str):
    if not (new_name[0].isupper() & new_name.isalnum()):
        raise Exception("Invalid")
    cls.__name__ = new_name