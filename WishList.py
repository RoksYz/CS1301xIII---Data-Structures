def wish_list(Wish,Pitem,Cost,Budget):
    if Pitem in Wish:
        if Budget >= item_cost:
            return "You should buy a {}".format(Pitem)
        else:
            return "You should save up for a {}!".format(Pitem)
    else:
        return "You probably don't want to buy a {}.".format(Pitem)


#print: "You should save up for a bugle!"
wish_list_items = ["bugle", "trumpet", "banjo", "tuba"]
selected_item = "bugle"
item_cost = 37.79
budget = 46.76

print(wish_list(wish_list_items, selected_item, item_cost, budget))
