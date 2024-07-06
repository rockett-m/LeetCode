class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        if len(enemyEnergies) == 0: return 0
        points = 0
        enemyEnergies.sort()
        lp, rp = 0, len(enemyEnergies)-1
        while lp <= rp:
            # get points first because with that 
            # you can gain energy (low to high sort)
            if currentEnergy >= enemyEnergies[lp]:
                ratio = currentEnergy // enemyEnergies[lp]
                currentEnergy -= ratio*enemyEnergies[lp]
                points += ratio
                # lp += 1
            elif points >= 1:
                currentEnergy += enemyEnergies[rp]
                rp -= 1
            else:
                break

        return points