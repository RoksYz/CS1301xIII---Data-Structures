

def most_oscars(Adict):
    value = 0
    key = ""
    for keys,values in Adict.items():
        if values > value:
            value = values
            key =  keys
        else:
            pass

    Final = (key,value)

    return Final
#print: ('Meryl Streep', 20)
nominees = {'Meryl Streep': 20, 'Robert De Niro': 7, 'Michael Caine': 6, 'Maggie Smith': 6}
print(most_oscars(nominees))
