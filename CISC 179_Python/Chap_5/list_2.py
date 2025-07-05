example = [1, 2, 3, 4]
example
example[3] = 0
example

numbers = [2, 3, 4, 5]
numbers
for index in range(len(numbers)):
    numbers[index] = numbers[index] ** 2
numbers

sentence = "This example has five words."
words = sentence.split()
words
for index in range(len(words)): words[index].upper()
words