def course_info(listuple):
    students = []
    avg_age = 0
    for items in listuple:
        students.append(items[0])
        avg_age+=items[1]
    
    avg_age = avg_age / len(listuple)

    Finaldict = {}
    Finaldict["students"] = students
    Finaldict["avg_age"] = avg_age

    return Finaldict

print(course_info([("Jackie", 20), ("Marguerite", 21)]))

