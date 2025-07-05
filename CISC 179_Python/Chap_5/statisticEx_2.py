# Put your code here
import collections

def getNumbers():
    nums = []     # start with an empty list

    # sentinel loop to get numbers
    numInput = input("Enter a number (<Enter> to quit):")
    while numInput != "":
        x = eval(numInput)    # convert to int
        nums.append(x)        # add this value to the list
        numInput = input("Enter a number (<Enter> to quit):")
    return nums
    
def median(nums):
    #check for empty list
    if len(nums) == 0:
        return 0
    nums.sort()
    #print("sorted list:",nums)
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0:
        median = (nums[midPos] + nums[midPos-1]) / 2.0
    else:
        median = nums[midPos]
    return median

def mod(nums):
    #check for empty list
    if len(nums) == 0:   
        return 0
    return(max(set(nums), key=nums.count))

def mode(nums):
    #check for empty list
    if len(nums) == 0:
        return 0
    # calculate the frequency of each item
    data = collections.Counter(nums)
    data_list = dict(data)

    # Print the items with frequency
    # print(data_list)

    # Find the highest frequency
    max_value = max(list(data.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    if len(mode_val) == len(nums):
        #print("No mode in the list")
        return 0
    else:
        #print("The Mode of the list is : " + ', '.join(map(str, mode_val)))
        return mode_val


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
    med = median(data)
    
    modSimple = mod(data)
    
    print("Mode:",modData[0])
    print("Median:", med)
    print("Mean:", xbar)
    print("Mod:", modSimple)

if __name__ == '__main__': 
    main()
