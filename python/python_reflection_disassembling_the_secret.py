def find_the_secret(f):
    return [i for i in f.__code__.co_consts if len(str(i)) == 32][0]