def abstract_names(listoflist):
    Finaldict = {}
    for item in listoflist:
        for items in item:
            items = items.split()
            item0 = items[0]
            if item0  not in Finaldict:
                Finaldict[item0]=[items[1]]
            else:
                Finaldict[item0]+=[items[1]]
                
    for values in Finaldict.values():
        values.sort()
    return Finaldict
            

#print (although the order of the keys may vary):
#{"David": ["Beckham", "Joyner", "Tennant"], "Ananya": ["Agarwal", "Birla", "Chatterjee", "Roy"], "Inés": ["Melchor", "Sainz", "Suarez"]}
names = [["David Joyner", "David Tennant", "David Beckham"], ["Ananya Birla", "Ananya Agarwal", "Ananya Chatterjee", "Ananya Roy"], ["Ines Sainz", "Ines Suarez", "Ines Melchor"]]
print(abstract_names(names))
