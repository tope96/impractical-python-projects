"""Generate funny names by randomly combining names from 2 separate lists."""
import sys
import random

def main():
    """Choose names at random from 2 tuples of names and print to screen."""
    print("Welcome to the Psych!")

    first = ("Baby oil", "Bad News", "Big Burps",
             "Bill", "Butterbean", "Buttermilk")

    last = ("Appleyard", "Bigmeat", "Bloominshine",
            "Guster", "Pealike", "Whipkey")

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        print("\n\n")
        print("{} {}".format(first_name, last_name), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit")

if __name__ == "__main__":
    main()
