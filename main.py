# BJC, Original Author
# 3/1/2024
# Main.py iniitates the quiz module, so far
import ascii_art

def print_instructions():
    print(ascii_art.welcome_msg)
    print("\nHello, and welcome to the population genetics module! This tool has many features,\nincluding a quiz function and a calculation function, to name a few.\n")
    username = input("\nPlease enter your name: ")
    print("\nGreetings", username)
    print("\nWhich section would you like to enter? Type [Q] to enter the quiz portion, or type [C] to enter the calculator portion.")
    module_selection = input("\nPlease enter your selection: ")
    return module_selection

def main():
    # Maybe it would be best to insert a different document to initialize
    # questions
    print_instructions()



if __name__ == "__main__":
    main()
