import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zeros = threading.Semaphore(1)
        self.evens = threading.Semaphore(0)
        self.odds = threading.Semaphore(0)
        # wait, [action], clear, set

	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        # start with 1
        for i in range(1, self.n+1):
            self.zeros.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.evens.release()
            else:
                self.odds.release()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n+1, 2):
            self.evens.acquire()
            printNumber(i)
            self.zeros.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for j in range(1, self.n+1, 2):
            self.odds.acquire()
            printNumber(j)
            self.zeros.release()
