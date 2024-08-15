

direction = input("Which direction? ").lower()
match direction:
    case "north":
        print("Up")
    case "east":
        print("Right")
    case "south":
        print("Down")
    case "west":
        print("Left")
    case _:
        print("Not a valid direction!")