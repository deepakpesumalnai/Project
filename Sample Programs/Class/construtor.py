from abc import ABC, abstractmethod
from typing import AsyncIterator, Dict, Mapping, Tuple

class AbstractClassExample(ABC):
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i
        print("abclass")

        @abstractmethod
        def get_data(self):
            pass
    @abstractmethod
    def read_all_addresses(self) -> AsyncIterator[Tuple[str, AddressEntry]]:
        raise NotImplementedError()

class ComplexNumber(AbstractClassExample):
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i
        print("subclass")

    def get_data(self):
        print(f'{self.real}+{self.imag}')
        value = self.real + self.imag
        print(value)


# Create a new ComplexNumber object
num1 = ComplexNumber(2, 3)

# Call get_data() method
# Output: 2+3j
num1.get_data()

# Create another ComplexNumber object
# and create a new attribute 'attr'
#num2 = ComplexNumber(5)
#num2.attr = 10

# Output: (5, 0, 10)
#print((num2.real, num2.imag, num2.attr))
