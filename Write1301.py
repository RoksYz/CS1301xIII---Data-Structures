def write_1301(filename,tuplelist):
    FileOpen = open(filename,'w')

    for item in tuplelist:
        
        ss = str(item)
        ss = ss.replace("[","")
        ss = ss.replace("]","")
        ss = ss.replace("(","")
        ss = ss.replace(",","")
        ss = ss.replace('"',"")
        ss = ss.replace("'","")
        ss = ss.replace(")","")
        
        FileOpen.write(ss+"\n")

    FileOpen.close()

tuple1 = (1, "exam_1", 90, 100, 0.6)
tuple2 = (2, "exam_2", 95, 100, 0.4)
tupleList = [tuple1, tuple2]
write_1301("output.cs1301", tupleList)

