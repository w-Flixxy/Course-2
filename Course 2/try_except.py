print("before")
try:
    #4 / 0
    print(name)
except NameError as e:
    print("This was a name error")
    print(e)
except ZeroDivisionError:
    print ("This was a zerodivision error")
class CheeseError(Exception):
    pass
print("after")

def upper_fun(word):
    if len(word) <= 0:
        raise CheeseError("The word has to be at least 1 letter!")
    return word.upper()

print(upper_fun(""))