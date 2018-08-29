def string_splitter(TestS):
    stringlist = []
    string = ""
    for s in TestS:
        if s  ==" ":
            stringlist.append(string)
            string = ""
        else:
            string+=s
    
    if string:
        stringlist.append(string)
    else:
        pass
    
    return stringlist

#print: ['Hello', 'world']
print(string_splitter("Hello world"))
