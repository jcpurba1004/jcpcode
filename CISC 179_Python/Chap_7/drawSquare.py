import turtle 

def square(t, length):
    #Draws a square with the given length
#    for count in range(4):
        t.forward(length)
        t.left(90)

def hexagon(t, length):
    #Draws a hexagon with the given length
#    for count in range(6):
        t.forward(length)
        t.left(60)

def main():
    t = turtle.Turtle()
    length = 50
    square(t,length)
    length = 100
    hexagon(t,length)

if __name__ == "__main__":
    main()
