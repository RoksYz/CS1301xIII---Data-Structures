def next_fib(listint,singleint):
    modlist = listint
    for s in range(singleint):
       countsum =  modlist[-1] + modlist[-2]
       modlist.append(countsum)
    
    return modlist

a_list = [5, 5, 10, 15, 25, 40, 65]
print(next_fib(a_list, 3))