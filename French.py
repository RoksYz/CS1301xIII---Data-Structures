french_dict = {"me": "moi", "hello": "bonjour", 
               "goodbye": "au revoir", "cat": "chat", 
               "dog": "chien", "and": "et"}

def french2eng(string):
    string = string.lower()
    string = string.split()
    newstring = []
    for item in string:
        if item in french_dict.keys():
            newstring.append(french_dict[item])

        else:
            newstring.append(item)

    newstring = ' '.join(newstring)
    return newstring
            
    
print(french2eng("Hello it's me"))