def write_weird_file(FileName,List,mode="w",sort_first=False,reverse_first=False):
    files = open(FileName,mode)

    if sort_first == True:
        List.sort()

    if reverse_first == True:
        List.reverse()

    for item in List:
        files.write(str(item)+"\n")
    files.close()


#Print:
#Wait, where'd the other text go?
#It's gone!
#3
#2
#1
write_weird_file("output.txt", ["Hmm, I bet this text will disappear.", "I wonder where it will go?"])
write_weird_file("output.txt", ["Wait, where'd the other text go?", "It's gone!"])
write_weird_file("output.txt", [2, 1, 3], mode="a", sort_first=True, reverse_first=True)