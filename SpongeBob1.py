
def mock(string):
    result = ""
    yn = True
    for s in string:
        if yn:
            result+=s.upper()
        else:
            result+=s.lower()
        yn = not yn 
    return result



print(mock("abcd efgh ijkl"))



