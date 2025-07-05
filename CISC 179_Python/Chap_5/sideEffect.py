first = [10, 20, 30]
second = first
first
second
first[1] = 99
first
second

third = []
for element in first:
    third.append(element)
first
third
first[1] = 100
first
third

third = list(first)