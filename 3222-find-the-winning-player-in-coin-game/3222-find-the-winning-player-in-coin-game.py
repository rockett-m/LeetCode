class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        count = 0
        while x > 0 and y > 0:
            if y < 4:
                break

            count += 1
            x -= 1
            y -= 4

        return "Bob" if count % 2 == 0 else "Alice"
