def input_type(s):
    if s == "True":
        return "boolean"
    elif s == "False":
        return "boolean"
    elif s == "":
        return "string"
    elif s.isdigit():
        return "integer"
    else:
        return "float"

print(input_type(""))
print(input_type("False"))
print(input_type("7.432621"))
print(input_type("2788"))