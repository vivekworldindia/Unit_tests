def main():
    x = int(input("what's x? "))
    #  x = input("what's x? ")
    print("x square is ", square(x))
    
def square(n):
    return n*n

if __name__ == "__main__":
    main()