class Solution:
    def checkRecord(self, s: str) -> bool:
        count = Counter(s)
        if count['A'] >= 2:
            return False

        late_count = 0
        prev = ''
        for idx, let in enumerate(s):
            print(idx, let)

            if let == 'L':
                late_count += 1
            elif let != 'L':
                late_count = 0
            if late_count >= 3:
                return False
            print(late_count)
            prev = let
        return True
