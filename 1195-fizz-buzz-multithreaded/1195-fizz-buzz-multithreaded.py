from threading import Event, Semaphore
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fizzs = Semaphore(0)
        self.buzzs = Semaphore(0)
        self.fbs = Semaphore(0)
        self.nums = Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 != 0:
                self.fizzs.acquire()
                printFizz()
                self.nums.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i % 5 == 0 and i % 3 != 0:
                self.buzzs.acquire()
                printBuzz()
                self.nums.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 == 0:
                self.fbs.acquire()
                printFizzBuzz()
                self.nums.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.nums.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.fbs.release()
            elif i % 3 == 0:
                self.fizzs.release()
            elif i % 5 == 0:
                self.buzzs.release()
            else:
                printNumber(i)
                self.nums.release()
