code = input("Enter the coded text: ")
distane = int(input("Enter the distance value: "))
plainText = ""
for ch in code:
    ordervalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - (distance - (ord('a') - ordvalue -1))
    plainText += chr(cipherValue)
print(plainText)