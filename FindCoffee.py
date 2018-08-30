def find_coffee(filename):
    result = ""
    files = open(filename,"r")
    reads = files.readlines()
    for s in reads:
        result+=s

    if "coffee" in result:
        return True
    else:
        return False
    files.close()
print(find_coffee("coffeeful.txt"))
