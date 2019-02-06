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

def cities():
    yield 'bangalore'
    yield 'mangalore'
    yield 'mysore'
    yield 'tumkur'
    yield 'shivamogga'
    yield 'bellary'

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

    return

    places = cities()
    while places: 
        try:
            print(next(places))
        except StopIteration:
            break

    print(line('-'))

    for city in cities():
        print(city)

    # names = ['vinod', 'shyam', 'harish', 'ramesh']

    # for name in names: print(name)

    # print(line('-'))

    # names_itr = iter(names)
    # while names_itr:
    #     try:
    #         print(next(names_itr))
    #     except StopIteration:
    #         break

if __name__ == '__main__':
    main()