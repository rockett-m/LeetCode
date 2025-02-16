class Solution:
    def canWinNim(self, n: int) -> bool:
        # remove 1 to 3 stones per turn
        # removing last stones on board wins
        # whoever's turn it is with 4 stones left will lose
        if n % 4 != 0: return True
        # so if we can get it down to 3 stones on our turn - win
        return False
