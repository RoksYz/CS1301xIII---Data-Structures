def count_types(Astring):

    Adict = {}
    characters = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
    characters0 = "'"

    for item in Astring:
        if item.isupper():
            if "upper"  not in Adict:
                Adict["upper"]=1
            else:
                Adict["upper"]+=1
        if item.islower():
            if "lower"  not in Adict:
                Adict["lower"]=1
            else:
                Adict["lower"]+=1

        if item.isnumeric():
            if "numeral"  not in Adict:
                Adict["numeral"]=1
            else:
                Adict["numeral"]+=1

        if item.isspace():
            if "space"  not in Adict:
                Adict["space"]=1
            else:
                Adict["space"]+=1
        if item in characters or item in  characters0:
            if "punctuation"  not in Adict:
                Adict["punctuation"]=1
            else:
                Adict["punctuation"]+=1

    return Adict







#print (although the order of the keys may vary):
#{"lower": 7}
#{"upper": 3, "lower": 8, "punctuation": 1, "spaces": 4, "numerals": 3}
print(count_types("aabbccc"))
print(count_types("ABC 123 doe ray me!"))
