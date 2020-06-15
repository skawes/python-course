def printString(text="hello"):
    string = "hello"
    print(text)
    list_display = ["awes", "awes"]
    print(list_display)
    print("hello", "hhghghg", text)


printString("")


def add(a, b):
    print("The sum of", a, "and", b, "is", a + b)


add(a=8, b=8)


def string(a: str, b: str):
    if a == "" and b == "":
        return ""
    return a + " " + b


print(string("", ""))
