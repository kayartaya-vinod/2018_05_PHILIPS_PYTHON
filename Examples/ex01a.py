class Product(object): 

    author = 'Vinod'
    refs = []

    def __init__(self, author):
        self.author = author
        self.refs.append(self)


def line():
    print('-'*50)

def main():
    p1 = Product('KVinod') 
    p2 = Product('Kumar')

    print('Product.author is', Product.author)
    print('id(Product.author) is', id(Product.author))
    line()
    print('p1.author is', p1.author)
    print('id(p1.author) is', id(p1.author))
    line()
    print('p2.author is', p2.author)
    print('id(p2.author) is', id(p2.author))
    line()

    print('Total references = ', len(Product.refs))

if __name__ == '__main__':
    main()







