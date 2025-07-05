textInput = input("Enter a string of bits: ")
textInput = textInput[-1] + textInput[:-1]
print(textInput)