
def find_max_sales(Lt):
    Compare = 0
    TopName = ""

    for item in Lt:

        if item[1] > Compare:
            Compare = item[1]
            TopName = item[0]
        else:
            pass

    return TopName

#print: Rogue One
movie_list = [("Finding Dory", 486), ("Captain America: Civil War", 408), ("Deadpool", 363), ("Zootopia", 341), ("Rogue One", 529), ("The Secret Life of Pets", 368), ("Batman v Superman", 330), ("Sing", 268), ("Suicide Squad", 325), ("The Jungle Book", 364)]
print(find_max_sales(movie_list))

