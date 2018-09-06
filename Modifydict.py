def modify_dict(adict):
    adict01 = adict
    for items in list(adict):
        if items[0].isupper():
            pass
        else:
            del adict01[items]
    return adict01
#print (although the order of the keys may vary):
#  {'Diaddigo':'Joshua', 'Elliott':'jackie'}
my_dict = {'Joshua':'Diaddigo', 'joyner':'David', 'Elliott':'jackie', 'murrell':'marguerite'}
print(modify_dict(my_dict))