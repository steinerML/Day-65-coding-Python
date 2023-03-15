def my_decor(func):
    def wrap():
        print('Here the wrap')
        func()
    return wrap

def my_poo():
    print("This is my poo")

my_try = my_decor(my_poo)
my_try()

#Is equivalent to:

def my_decor(func):
    def wrap():
        print('Here the wrap')
        func()
    return wrap

@my_decor
def my_poo():
    print("This is my poo")
my_poo()
