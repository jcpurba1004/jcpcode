def fun(a,b,c,d):
    print(a,b,c,d)

def main():
    myList = [1,2,3,4]
    myTuple = (5,6,7,8)
    fun(*myList)
    fun(*myTuple)

if __name__ == '__main__':
    main()