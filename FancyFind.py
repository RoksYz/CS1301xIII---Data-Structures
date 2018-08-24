
def fancy_find(search_within,search_for):
    s = search_within.find(search_for)
    if search_within.find(search_for) >= 0:
        return("{} found at index {}!".format(search_for,s))
    else:
        return("{} was not found within {}!".format(search_for,search_within))

print(fancy_find("ABCDEF", "DEF"))
print(fancy_find("ABCDEF", "GHI"))