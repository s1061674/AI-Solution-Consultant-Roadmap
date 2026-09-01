class EvenNumbers:

    def __init__(self, max_value):
        self.max_value = max_value
        self.start = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.max_value:
            raise StopIteration
        
        value = self.start
        self.start += 2
        return value
    
numbers = EvenNumbers(10)

for number in numbers:
    print(number)