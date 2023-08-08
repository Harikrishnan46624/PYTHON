
def gen():
    yield 10
    yield 20
    yield 30
g = gen()
print(g.__next__())


class A:
    def __init__(self) -> None:
        pass