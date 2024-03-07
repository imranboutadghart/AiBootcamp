import sys
import string


def calculate(str):
    """
    calculate(str) : returns the number of uppercase,
    lowercase, punctuations, digits, spaces, punctuations in a string
    """
    upper = 0
    lower = 0
    digits = 0
    spaces = 0
    punctuations = 0
    for c in str:
        if (c.isupper()):
            upper += 1
        elif (c.islower()):
            lower += 1
        elif (c.isdigit()):
            digits += 1
        elif (c.isspace()):
            spaces += 1
        elif (c in string.punctuation):
            punctuations += 1
    return (upper, lower, punctuations, digits, spaces)


def main():
    if len(sys.argv) > 2:
        print("AssertionError")
        exit()
    if len(sys.argv) < 2:
        str = input()
    else:
        str = sys.argv[1]
    (upper, lower, punctuations, digits, spaces) = calculate(str)
    print("""The text contains {} characters:\n{} upper letters
{} lower letters\n{} punctuation marks\n{} spaces
{} digits""".format(len(str), upper, lower, punctuations, spaces, digits))


if __name__ == "__main__":
    main()
