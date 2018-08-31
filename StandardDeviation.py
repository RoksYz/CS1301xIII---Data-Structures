
def st_dev(filename):
    files = open(filename,"r")

    mean = 0
    count = 0
    lisst = []
    for item in files:
        lisst.append(item)
        mean+=int(item)
        count+=1   
    resultmean = mean / count

    resultdifs = 0
    for items in lisst:
        dif = int(items) - resultmean
        square = dif ** 2
        resultdifs += square 

    
    Result = resultdifs / count
    FinalResult = Result ** 0.5

    return FinalResult



    files.close()
    

#print 27.796382658340438 (or something around there).
print(st_dev("some_numbers.txt"))
