def attendance_check(roster,present):
    result = []
    for s in roster:
        if s not  in present:
            result.append(s)
    result.sort()
    return result


#['Ferguson', 'Winston']
test_roster = ['Jessica', 'Nick', 'Winston', 'Schmidt', 'Cece', 'Ferguson']
test_present = ['Nick', 'Cece', 'Schmidt', 'Jessica']
print(attendance_check(test_roster, test_present))