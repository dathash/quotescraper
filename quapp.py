from typing import List, Dict
import random
import os
import time


def organize(filename: str) -> Dict[str, List[str]]:
    """
    Takes a filename, and organizes the data therein into a dict with
    Authors as the key and a list of that author's quotes as the value.
    """
    register: Dict[str, List[str]] = {}
    author_quotes = read_quotes(filename)
    for instance in author_quotes:
        splitstance = instance.split("  |  ")  # List with author and quote.
        if splitstance[0] not in register:
            register[splitstance[0]] = [splitstance[1]]
        else:  # If author already has a quote in the register...
            register[splitstance[0]].append(splitstance[1])
    return register


def read_quotes(filename: str) -> List[str]:
    """
    A helper function for organize(). Does file input.
    """
    fp = open(filename, "r", newline='')
    quotes = [x.strip() for x in fp.readlines()]
    fp.close()
    return quotes


def startupio() -> str:
    """
    Asks for a command and returns. User chooses Author, Keyword, or All.
    """
    while True:
        print("Limit search by Author with keyword 'Author'")
        print("Limit search by Keyword with keyword 'Keyword'")
        print("Perform search on all quotes with keyword 'All'\n")
        command = input()
        if command in ["Author", "Keyword", "All"]:
            os.system("cls")
            return command
        print("Keyword was formatted incorrectly. To remind you...")


def limiter(register: Dict[str, List[str]], command1: str) -> Dict[str, List[str]]:
    """
    Uses the command passed as an argument and calls on input functions to get
    a limiter. Limiter is then used to limit the search space according to user
    input. Supports all three first commands.
    """
    if command1 == "Author":
        auth_name = author_input(register)
        return {auth_name: register[auth_name]}
    elif command1 == "Keyword":
        keyword = keyword_input(register)
        new_register = {}
        for author in register:
            for quote in register[author]:
                if keyword in quote:
                    if author not in new_register:
                        new_register[author] = [quote]
                    else:
                        new_register[author].append(quote)
        return new_register
    elif command1 == "All":
        return register


def author_input(register: Dict[str, List[str]]) -> str:
    """
    Requests from the user a properly formatted
    author's name that is in the register.
    """
    while True:
        print("Please enter an Author's name, with Capitalization.")
        print("For suggestions of popular authors, type 'Suggestion'")
        auth_name = input()
        if auth_name in register:
            os.system("cls")
            return auth_name
        elif auth_name == "Suggestion":
            print("\nOscar Wilde, Albert Einstein, Mahatma Gandhi,\nAlbert Camus, John Green, Marilyn Monroe\n")
        else:
            print("That name is not in the directory. Try another formatting or another name.")


def keyword_input(register: Dict[str, List[str]]) -> str:
    """
    requests from the user a properly formatted
    keyword that is in at least one quote in the register.
    """
    while True:
        print("Please enter a Keyword.")
        print("For suggestions of popular keywords, type 'Suggestion'")
        keyword = input().lower()
        if keyword == 'suggestion':
            print("\nLove, Life, God, Time, Book, Books, Truth, Honesty, Courage, Death, Change, World\n")
        else:
            for author in register:
                for quote in register[author]:
                    if keyword in quote:
                        os.system("cls")
                        return keyword
            print("No quote contains that keyword. Try another keyword.")


def searchio() -> str:
    """
    Asks the user for a command - Either List or Random.
    """
    while True:
        print("For the entire list of items in the category, use 'List'")
        print("For a random quote from this category, use 'Random'\n")
        command = input()
        if command in ["List", "Random"]:
            os.system("cls")
            return command
        print("Command was formatted incorrectly. To remind you...")


def print_result(register: Dict[str, List[str]], command2: str):
    """
    Uses the search parameter to search through the register and
    return either a list of all items in the register, or a random element.
    """
    print("Your Results:\n")
    quotes = []
    for author in register:
        for quote in register[author]:
            quotes.append(author + "  |  " + quote)
    if command2 == "List":
        for quote in quotes:
            print(quote)
        print("Your search returned {} results".format(len(quotes)))
    if command2 == "Random":
        while True:
            print(random.choice(quotes))

            while True:
                inp = input("Want another in this category? y/n: ")
                if inp == "n":
                    return
                if inp != "y":
                    print("Improperly formatted. y/n")
                else:
                    os.system("cls")
                    break



def main():
    """ Driver for the program. """
    orig_register = organize("output.txt")
    os.system("cls")
    print("Welcome to Quapp v0.2!")
    time.sleep(2)
    os.system("cls")
    while True:
        print("Please enter a command.\n")
        register = orig_register.copy()
        command1 = startupio()
        register = limiter(register, command1)

        command2 = searchio()
        print_result(register, command2)
        while True:
            inp = input("Search in another category? y/n: ")
            if inp == "n":
                print("Thank you for using Quapp v0.2. Goodbye!")
                return 0  # Finish program.
            elif inp != "y":
                print("Improperly formatted. y/n")
            else:
                os.system("cls")
                time.sleep(1)
                break


if __name__ == "__main__":
    main()
