def character_info(sonly):
    result = ""
    ponto = ("[","]","/","^","_","`")
    if ord(sonly) in range(48,58):
        result = "number"
    elif sonly in ponto:
        result = "punctuation"
    elif ord(sonly) in range(65,123):
        result = "letter"
    else:
        result =  "punctuation"
    return (sonly,ord(sonly),result)

print(character_info("q"))
print(character_info("7"))
print(character_info("`"))
