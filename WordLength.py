def word_lengths(astring):

    replacex ='?.,!"'
    for item in replacex:
        astring = astring.replace(item,"")

    astring = astring.lower()
    astring = astring.split()

    Resultdict = {}
    for items in astring:
        value = len(items)
        Resultdict[items]=value
    
    return Resultdict
        
#print:
#{'dog': 3, 'today': 5, 'of': 2, 'ate': 3, 'bowl': 4, 'out': 3, 'a': 1, 'cereal': 6, 'i': 1}
#
#The order of the keys may differ, but that's okay!
print(word_lengths("I ate a bowl of cereal out of a dog bowl today."))