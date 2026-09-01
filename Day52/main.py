class Countdown:

    def __init__(self, countdown):
        self.countdown = countdown

    def __iter__(self):
        return self

    def __next__(self):
        if self.countdown <= 0:
            raise StopIteration
        
        value = self.countdown
        self.countdown -= 1
        return value
        
countdown = Countdown(5)

for value in countdown:
    print(value)