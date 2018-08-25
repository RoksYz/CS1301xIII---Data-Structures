
def valid_char(s):
    s = ord(s)
    if s in range(33,127):
            return True
    else:
            return False

print(valid_char("a"))
print(valid_char(" "))
print(valid_char("!"))
print(valid_char("☺"))
