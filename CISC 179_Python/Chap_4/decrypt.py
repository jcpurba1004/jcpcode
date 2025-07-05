code = input("Enter the coded text: ")
distance = int (input("Enter the distance value:"))
plainText =  ""
for ch in code:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    plainText += chr(cipherValue)
print(plainText)