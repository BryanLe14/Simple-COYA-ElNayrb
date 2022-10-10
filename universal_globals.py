import os, math

width = os.get_terminal_size()[0]
height = os.get_terminal_size()[1]
width2 = width / 2
height2 = height / 2
floorwidth2 = math.floor(width / 2)
floorheight2 = math.floor(height / 2)

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def enter_to_continue(pre="\n", post="\n"):
    return input(f"{pre}Enter to continue...{post}")