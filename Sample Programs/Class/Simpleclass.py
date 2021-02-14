print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__)))


class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Parent')


# Output: 10
#print(Person.age)

# Output: <function Person.greet>
#print(Person.greet)

# Output: 'This is my second class'
#print(Person.__doc__)


#harry = Person()

#print(harry.__doc__)
#print(harry.age)
#print(harry.greet)
