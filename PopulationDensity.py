def population_density(listdict):
    allpopulations = 0
    allarea = 0
    for item in listdict:
        s = list(item.values())
        allpopulations+=s[1]
        allarea+=s[2]
    return allpopulations / allarea
        
#print: 133.886 (or something around there)
countries = [{"name": "China", "population": 1390700000, "area": 9640821},
             {"name": "India", "population": 1348003000, "area": 3287240},
             {"name": "United States", "population": 325300000, "area": 9826675},
             {"name": "Indonesia", "population": 237556363, "area": 1904569}]
print(population_density(countries))
             