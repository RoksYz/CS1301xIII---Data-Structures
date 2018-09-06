def name_counts(Alist):
    dictotal = {}
    for item in Alist:
        item = item.split()
        if item[0] in dictotal:
            dictotal[item[0]]+=1
        else:
            dictotal[item[0]]=1

    return dictotal
#print (although the order of the keys may vary):
#{'Shelba': 5, 'Maren': 1, 'Nicol': 1, 'David': 2, 'Brenton': 2}
name_list = ["David Joyner", "David Zuber", "Brenton Joyner",
             "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
             "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
             "Shelba Fry", "Maren Fry"]
print(name_counts(name_list))
