
def find_color(string):
    ss = string.split('rgb')
    ss = ss[1].split(',')
    ss = str(ss)
    ss = ss.replace("(","")
    ss = ss.replace(")","")
    ss = ss.replace("[","")
    ss = ss.replace("]","")
    ss = ss.replace(",","")
    ss = ss.replace("'","")
    ss = ss.split()

    red_val = int(ss[0])
    green_val = int(ss[1])
    blue_val = int(ss[2])

    if red_val == green_val and red_val == blue_val:
        return "gray"
    elif red_val > green_val and  red_val > blue_val:
        return "red"
    elif blue_val > red_val and blue_val > green_val:
        return "blue"
    elif green_val > red_val and green_val > blue_val:
        return "green"
    elif red_val == green_val  != blue_val:
        return "yellow"
    elif red_val == blue_val != green_val:
        return "purple"
    elif green_val == blue_val:
        return "teal"

print(find_color("rgb(125, 50, 75)"))
print(find_color("rgb(0, 50, 50)"))
print(find_color("rgb(217, 217, 217)"))