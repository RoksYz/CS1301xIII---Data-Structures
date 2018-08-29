def one_dimensional_booleans(bool_list,use_and):
    if use_and == True:
        if False in bool_list:
            return False
        else:
            return True
    else:
        if True in bool_list:
            return True
        else:
            return False

#print: True, False, True, False.
print(one_dimensional_booleans([True, True, True], True))
print(one_dimensional_booleans([True, False, True], True))
print(one_dimensional_booleans([True, False, True], False))
print(one_dimensional_booleans([False, False, False], False))