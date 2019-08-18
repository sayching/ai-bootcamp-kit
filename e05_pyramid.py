# You will create a function that generates a pyramid

def pyramid(n, symbol, is_reverse):

    symbol = symbol + " "
    k = 2 * n - 2

    if is_reverse == True:
        for i in range(n, 0, -1):
            print((n - i) * ' ' + i * symbol)
    else:
        for i in range(0, n):
            for j in range(0, k):
                print(end=" ")
            k = k - 1
            for j in range(0, i + 1):
                print(symbol, end="")
            print("\r")

pyramid(6, "#", False )



