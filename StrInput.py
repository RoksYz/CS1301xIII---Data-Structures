def string_type(s):
    if s == "":
        return "empty"
    elif s == s[0]:
        return "character"
    elif len(s.split()) < 2:
        return "word"
    elif "\n" in s:
        return "page"
    elif "  "  and ". " in s:
        return "paragraph"
    else:
        return "sentence"


print(string_type(""))
print(string_type("!"))
print(string_type("CS1301."))
print(string_type("This is too many cases!"))
print(string_type("There's way too many ostriches. Why are there so many ostriches. The brochure said there'd only be a few ostriches."))
print(string_type("Paragraphs need to have multiple sentences. It's true.\nHowever, two is enough. Yes, two sentences can make a paragraph."))