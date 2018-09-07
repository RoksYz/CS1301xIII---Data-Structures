def length_words(astring):

    replacex ='?.,!"'
    for item in replacex:
        astring = astring.replace(item,"")
    
    astring = astring.lower()
    astring = astring.split()


    Resultdict = {}
    for items in astring:
        value = len(items)
        if value not in Resultdict:
            Resultdict[value]=[items]
        
        else:
            Resultdict[value].append(items)

    
    return Resultdict

#print:
#{1: ['i', 'a', 'a'], 2: ['of', 'of'], 3: ['ate', 'out', 'dog'], 4: ['bowl', 'bowl'], 5: ['today'], 6: ['cereal']}
#
#The keys may appear in a different order, but within each
#list the words should appear in the order shown above.
print(length_words("I ate a bowl of cereal out of a dog bowl today."))