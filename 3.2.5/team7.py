strategy_name = "Very funky thing"
def move(my_history, their_history):
    #program starts with rock always
    if len(my_history) == 0:
        return "r"
    #then the program checks if it lost or won
    elif len(their_history) > 0:
        if their_history[-1] == "r":
            if my_history[-1] == "s":
                return "p"
            else:
                if my_history[-1] == "p":
                    return "s"
                else:
                    return "s"
        if their_history[-1] == "p":
            if my_history[-1] == "r":
                return "s"
            else:
                if my_history[-1] == "s":
                    return "r"
                else:
                    return "r"
        if their_history[-1] == "s":
            if my_history[-1] == "p":
                return "r"
            else:
                if my_history[-1] == "r":
                    return "p"
                else:
                    return "p"