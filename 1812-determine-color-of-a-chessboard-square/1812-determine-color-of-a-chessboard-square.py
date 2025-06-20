class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:

        first = ord(coordinates[0]) - 96

        second = int(coordinates[1])

        return True if (first + second) % 2 == 1 else False
