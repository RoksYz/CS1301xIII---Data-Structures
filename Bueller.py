def students_present(adict):
    TheList = []
    for items in adict.items():
        if items[1] == "":
            pass
        else:
            TheList.append(items[0])

    return TheList

#print: ["David", "Marguerite", "Joshua", "Erica"]
student_list = {"David" : "Here", "Marguerite" : "Here",
                "Jackie": "", "Joshua": "Present",
                "Erica": "Here", "Daniel": ""}
print(students_present(student_list))

