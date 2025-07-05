sentence = input("Enter a sentence: ")
listOfWords = sentence.split()
print("There are", len(listOfWords), "words.")
sum = 0
for word in listOfWords: sum += len(word)
print("The average word length is", sum / len(listOfWords))

#<an object>.<method name>(<argument-1>,..., <argument-n>)

s = "Hi there!"
len(s)
s.center(11)
s.count('e')
s.endswith("there!")
s.startswith("Hi")
s.find("the")
s.isalpha()
'abc'. isalpha()
"326".isdigit()
words = s.split()
words
" ".join(words)
" ". join(words)
s.lower()
s.upper()
s.replace('i', 'o')
" Hi there! ".strip() 

"myfile.txt".split('.')
"myfile.py".split('.')
"myfile.html".split('.')

#filename.split('.')[-1]