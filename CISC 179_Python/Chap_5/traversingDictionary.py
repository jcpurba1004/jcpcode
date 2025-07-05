for key in info:
     print(key, info[key])

grades = {90:'A', 80:'B', 70:'C'}
list(grades.items())

for (key, value) in grades.items():
    print(key, value)

theKeys = list(info.keys())
theKeys.sort()
for key in theKeys:
    print(key, info[key])