'''
Module: ex01
Author: Vinod <vinod@vinod.co>
Version: 1.0
'''

class Product(object): 
    '''
    class Product
    has details of a product 
    mapped to the database columns (in the future)
    '''

    # class variable (cannot be accessed from member function)
    author = 'Vinod'

    # called automatically by python when an instance is constructed
    # and the reference of the newly constructed object is passed as the
    # first argument. We can add new attributes to "self" , which are
    # called as members of the object
    def __init__(self):
        self.id = 1
        self.name = 'Apple macbook pro'
        self.price = 1080000
        self.category = 'computers'

    def test(self):
        print(dir(self))
        print('while testing, id(self) is', id(self))
        # print('author is', author)
        self.author = 'KVinod'
        print('author is', self.author)


def main():
    p1 = Product() # new Product instance is created

    print('id(p1) is: ', id(p1))

    # the invoking reference is implicitly passed as the 
    # first argument to the invoked functon
    p1.test() # OOP style
    # Product.test(p1) # Procedural oriented approach
    print('Product.author is', Product.author)

    print('id(p1.author) is', id(p1.author))
    print('id(Product.author) is', id(Product.author))



# call the main() function only if this module is executed 
# from the command prompt
if __name__ == '__main__':
    main()







