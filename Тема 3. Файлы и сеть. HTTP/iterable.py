class MyIterable:
    def __init__(self, start, stop):
        if not stop > start:
            raise ValueError('Start has to be < than stop')

        self.start = start
        self.stop = stop
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        return self.current

it = MyIterable(stop=8, start=1)

print(next(it))


