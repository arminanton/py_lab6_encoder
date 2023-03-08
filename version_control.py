# version control encoder - lab 6
# Author: Guilherme Armin Da Silva Anton (aka Armin)
# Partner: Yutaka Stephens

# importing these two to handle script exit behaviour
import shlex
import sys

def encode(original):
    chars = []
    chars[:] = original
    encoded = ""
    for char in chars:
        num = int(char)
        num += 3
        encoded += f"{num}"
    return encoded

def decode(encoded):
    chars = [encoded]
    original = ""
    for char in chars:
        num = int(char) - 3
        original += f"{num}"
    return original

# main function
def main() -> int:
    original = ""
    encoded = ""

    while True:
        print("\nMenu")
        print("--------")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")

        option = input("\nPlease enter an option: ")

        if option == "1":
            if original == "":
                original = input("Please enter your password to encode: ")
                encoded = encode(original)
            print("Your password has been encoded and stored!")

        elif option == "2":
            if encoded == "":
                encoded = input("Please enter your password to decode: ")
                original = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {original}.")

        elif option == "3":
            break

        else:
            print("\nInvalid option")


# only executes main if file is being loaded as starter instead of
# imported as a module.
if __name__ == '__main__':
    sys.exit(main()) # executes main() and exits properly

