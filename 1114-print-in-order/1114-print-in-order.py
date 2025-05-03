class Foo:
    def __init__(self):
        self.print1 = threading.Event()
        self.print2 = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.print1.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.print1.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.print2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.print2.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()