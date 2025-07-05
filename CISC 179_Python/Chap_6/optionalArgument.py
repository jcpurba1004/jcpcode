def <function name>(<required arguments>,
                    <key-1> = <val-1>, ... <key-n> = <val-n>)

def repToInt(repString, base):
    """Converts the repString to an int in the base
    and returns this int."""
    decimal = 0
    exponent = len(repString) - 1
    for digit in repString:
        decimal = decimal + int(digit) * base ** exponent
        exponent -= 1
    return decimal

def repToInt(repString, base = 2):
    repToInt("10", 10)
    repToInt("10", 8)
    repToInt("10", 2)
    repToInt("10")

def example(required, optionl = 2, option2 = 3):
    print(required, optionl, option2)
example(1)
example(1, 10)
example(1, 10, 20)
example(1, option2 = 20)
example(1, option2 = 20, option1 = 10)