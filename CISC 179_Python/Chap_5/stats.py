from math import sqrt

def getNumbers():
    nums = []     # start with an empty list

    # sentinel loop to get numbers
    numInput = input("Enter a number (<Enter> to quit):")
    while numInput != "":
        x = eval(numInput)    # convert to int
        nums.append(x)        # add this value to the list
        numInput = input("Enter a number (<Enter> to quit):")
    return nums

def mode(nums):
    #check for empty list
    if len(nums) == 0:
        return 0
    return(max(set(nums),  key=nums.count))

def mean(nums):
    #check for empty list
    if len(nums) == 0:
        return 0

    sum = 0.0
    for num in nums:
        sum = sum + num
    return sum / len(nums)

def main():

    data = getNumbers()
    print("List:",data)
    xbar = mean(data)
    modData = mode(data)
#    med = median(data)

    print("Mode:",modData)
#    print("Median:", med)
    print("Mean:", xbar)

if __name__ == '__main__':
    main()