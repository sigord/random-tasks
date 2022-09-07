from typing import Iterable

def mysum(l : Iterable, start = 0):
    from functools import reduce
    from operator import add
    return start + reduce(add, l)

if __name__ == "__main__":
    a = input()
    a = list(map(int,a.split()))
    print(mysum(a))