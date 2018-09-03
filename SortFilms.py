def sort_films(filename,filedestination):
    FileOpen0 = open(filename,"r")
    listt = []
    for item in FileOpen0:
        item0 = item.split("\t")
        item1 = item0[1].strip("\n")
        listt.append(item1)
        listt.sort(reverse=True)

    i=0
    for i in range(len(listt)):
        FileOpen1 = open(filedestination,"a")
        for line in open(filename):
            line0 = line.split("\t")
            line1 = line0[1].strip("\n")
            if listt[i]==line1:
                print(line0[0]+'\t',line1,file=FileOpen1)
                i+=1
                break
            else:
                pass

    FileOpen0.close()

#print: "Done!"
sort_films("top500.txt", "top500result.txt")
print("Done!")