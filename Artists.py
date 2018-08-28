def sort_artists(tp):

    result =[]
    value =[]

    for s in tp:
        for item in s:
            try:
                if item.isnumeric:
                    result.append(item)  
            except:
                value.append(item)
    
    result.sort()
    value.sort(reverse=True)

    final = (result,value)
    return final

#(['Elvis Presley', 'Michael Jackson', 'The Beatles'], [270.8, 211.5, 183.9])  
artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
print(sort_artists(artists))


