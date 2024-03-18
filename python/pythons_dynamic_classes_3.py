# https://www.codewars.com/kata/pythons-dynamic-classes-number-3

def create_class(class_name, secrets={}): return None if not class_name else type(class_name, (object,), secrets)