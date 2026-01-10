# Una simple función generadora
from unittest import result


def my_gen():
    n = 1
    print('This is printed first')

    yield n

    n += 1
    print('This is printed second')

    yield n

    n += 1
    print('This is printed at last')

    yield n

# Devuelve un objeto generador
a = my_gen()

# Podemos iterar sobre los elementos usando la llamada 'next'
next(a)

# Una vez devolvemos el resultado con yield, la función se pausa y devuelve el control al usuario.
# Las variables locales y sus estados se recuerdan entre llamadas sucesivas.
next(a)

next(a)

#----------------------------------------------
# Initialize the list
my_list = [1, 3, 6, 10]
# square each term using list comprehension
list_ = [x**2 for x in my_list]
# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis
generator = (x**2 for x in my_list)
print(list_)
print(generator)

#----------------------------------------------
# largo y coionfuso
class PowTwo:
    def __init__ (self, max=0):
        self.n = 0
        self.max = max

    def __iter__ (self):
        return self
    
    def __next__ (self):
        if self.n > self.max:
            raise StopIteration
        
        result = 2 ** self.n
        self.n += 1
        return result

#------------------------------
def PowTwoGen (max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

#------------------------------

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        yield x
        x, y = y, x+y

print(list(fibonacci_numbers(10)))
   