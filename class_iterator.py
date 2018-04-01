#!/usr/bin/python

class AutoGenerator:
    def __init__(self,start,stop,step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def next(self):
        self.start += self.step
        if self.start >= self.stop:
            raise StopIteration
        return self.start

    def __iter__(self):
        return self

def main():
    a = AutoGenerator(0,100,1)
    for x in a:
        print(x)

if __name__ == "__main__":
    main()
