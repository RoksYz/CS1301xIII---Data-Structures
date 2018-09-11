def tire_pressure(listint):
    Reslt = []
    for item in listint:
        if item >= 15 and item <= 55:
            Reslt.append(item)
    FinalReslt = Reslt[-1]+Reslt[-2]+Reslt[-3]+Reslt[-4]+Reslt[-5]
    return FinalReslt / 5

#print: 35.0
a_list = [34, 34, 64, 34, 5, 5, 34, 34, 35, 35, 35, 65, 60, 35, 12, 35]
print(tire_pressure(a_list))

