class always_true:
    def __eq__(self, _):
        return True
    
omnibool = always_true()


print(omnibool == True and omnibool == False)