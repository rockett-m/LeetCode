class FrequencyTracker:

    def __init__(self):
        self.nums = {}
        self.freqs = {}

    def add(self, number: int) -> None:
        if number not in self.nums:
            self.nums[number] = 1
            if 1 not in self.freqs:
                self.freqs[1] = set()
            self.freqs[1].add(number)
        else:
            old_freq = self.nums[number]
            new_freq = old_freq + 1
            self.nums[number] = new_freq
            
            if len(self.freqs[old_freq]) == 1:
                del self.freqs[old_freq]
            else:
                self.freqs[old_freq].remove(number)
                if len(self.freqs[old_freq]) == 0:
                    del self.freqs[old_freq]
            if new_freq not in self.freqs:
                self.freqs[new_freq] = set()
            self.freqs[new_freq].add(number)

    def deleteOne(self, number: int) -> None:
        if number not in self.nums:
            return
        else:
            old_freq = self.nums[number]
            new_freq = old_freq - 1

            self.freqs[old_freq].remove(number)
            if len(self.freqs[old_freq]) == 0:
                del self.freqs[old_freq]
            if self.nums[number] == 1:
                del self.nums[number]
                return

            self.nums[number] = new_freq
            if new_freq not in self.freqs:
                self.freqs[new_freq] = set()
            self.freqs[new_freq].add(number)

    def hasFrequency(self, frequency: int) -> bool:

        return True if frequency in self.freqs else False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)