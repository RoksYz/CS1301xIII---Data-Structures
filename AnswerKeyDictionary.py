def calculate_score(studentan,correctan):
    if len(studentan) != len(correctan):
        return -1

    count = 0
    for items in studentan:

        if studentan[items] == correctan[items]:
            count+=1
        else:
            pass
            
    return count
#print: 3
student_answers = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
correct_answers = {1: "A", 2: "B", 3: "A", 4: "D", 5: "B"}
print(calculate_score(student_answers, correct_answers))