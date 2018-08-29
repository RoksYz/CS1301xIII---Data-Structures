def lucky_sevens(ListInt):
    seven = [7,7,7]
    if str(seven)[1:-1] in str(ListInt):
        return True
    
    return False
#print: True, then False
print(lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]))
print(lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]))