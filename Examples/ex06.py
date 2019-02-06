# about iterators and generators

line = lambda ch: ch*50

# once you use the 'yield' keyword, the function is called
# a generator, and the return value of this function can be
# treated as a iterable
def fibonacii(limit):
    a, b = -1, 1
    n = 1
    while n<=limit:
        c = a + b
        yield c

        a = b
        b = c
        n += 1

def main():

    fibo = fibonacii(100)
    # for n in fibo:
    #     print(n)

    for n in range(1, 10):
        num = next(fibo)
        print(num)

    print('=============')
    print(next(fibo))
    print(next(fibo))
    print(next(fibo))
    print(next(fibo))

if __name__ == '__main__':
    main()