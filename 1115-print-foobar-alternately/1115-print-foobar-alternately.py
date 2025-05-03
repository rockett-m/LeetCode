class FooBar:
    def __init__(self, n):
        self.n = n
        self.first = threading.Event()
        self.second = threading.Event()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            if i > 0: self.second.wait()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.second.clear()
            self.first.set()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.first.wait()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.first.clear()
            self.second.set()