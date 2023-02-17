

class A:
    def __init__(self):
        self.x = -1

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if self.x > 2:
            raise StopIteration
        else:
            self.x += 1
            return self.x

for i in A():
    print(i)

