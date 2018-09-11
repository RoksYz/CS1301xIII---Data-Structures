def write_movie_info(astring,adict):
    OpenFile = open(astring,"w")

    for dic in adict:
        AList = ""

        for keys,values in dic.items():
            keys = str(keys)
            values = str(values)
            keyitem = keys+": "
            AList+=keyitem
            AList+=values
            AList = AList.replace("[","")
            AList = AList.replace("]","")
            AList = AList.replace("'","")
            OpenFile.write(AList +"\n")
            AList = ""
#If your function works correctly, this will originally
#print nothing -- however, it should write the same contents
#as Sample.txt to Test.txt.
movies = [{"Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"], "Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}]
write_movie_info("Test.txt", movies)
