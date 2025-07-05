def main():
    """The main function for this script."""
    number = float(input("Enter a number: "))
    result = square(number)
    print("The square of", number, "is", result)

def square(x):
    """Returns the square of x."""
    return x * x

 The entry point for program execution
if __name__ == "__main__":
    main()

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase() + "."

def nounPhrase() :
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def main():
    """Allows the user to input the number of sentences to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())