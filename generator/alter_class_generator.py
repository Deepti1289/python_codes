#!/usr/bin/python

class AutoGenerator:
    def __init__(self,start,stop,step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def Next(self):
        self.start += self.step
        if self.start >= self.stop:
            raise StopIteration
        yield self.start

    def next(self):
        return self.Next().next()

    '''def __iter__(self):
        return self'''

def main():
    a = AutoGenerator(0,100,1)
    #print(next(a))
    #print(next(a))
    '''for b in a:
        print(b)'''
    x = a.next()
    print(x)
    x = a.next()
    print(x)
    
if __name__ == "__main__":
    main()
