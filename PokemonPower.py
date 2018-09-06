def total_stats(listdict):
    Finaldict = {}
    for items in listdict:
        total = 0
        string = ""

        for keys,values in items.items():
            if type(values) == str:
                string = values
            else:
                total+=values

        Finaldict[string]=total
    return Finaldict

            
            


#print (although the order of the keys may vary):
#{'Bulbasaur': 318, 'Charmander': 309, 'Squirtle': 314}
starters = [{"name": "Bulbasaur", "hp": 45, "attack": 49, "defense": 49, "special attack": 65, "special defense": 65, "speed": 45},
            {"name": "Charmander", "hp": 39, "attack": 52, "defense": 43, "special attack": 60, "special defense": 50, "speed": 65},
            {"name": "Squirtle", "hp": 44, "attack": 48, "defense": 65, "special attack": 50, "special defense": 64, "speed": 43}]
print(total_stats(starters))