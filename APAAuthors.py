def names_to_apa(string):

    string = string.split(',')
    Finalstring = ""
    for item in string:
        if " and " in item:
            item = item.split()
            Finalstring+="& "+item[2]+", "+item[1][:1]+"."
        else:
            item = item.split()
            Finalstring+=item[1]+", "+item[0][:1]+"., "

    return Finalstring

#print: Last, F., Joyner, D., & Burdell, G.
print(names_to_apa("First Last, David Joyner, and George Burdell"))
