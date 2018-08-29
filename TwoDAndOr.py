def two_dimensional_booleans(bool_list,use_and):
        Result = []
        if use_and == True:
            for item in bool_list:
                if False in item:
                    Result.append(False)
                else:
                    Result.append(True)
        else:
            for item in bool_list:

                if True in item:
                    Result.append(True)
                else:
                   Result.append(False)

        return Result

#print:
#[True, False, False]
#[True, True, False]
bool_superlist = [[True, True, True], [True, False, True], [False, False, False]]
print(two_dimensional_booleans(bool_superlist, True))
print(two_dimensional_booleans(bool_superlist, False))
