from functools import cache

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        def get_answer(spell):
            start = 0
            end = len(potions) - 1
            answer = -1
            while start <= end:
                mid = (start+end)//2
                val = potions[mid] * spell
                if val >= success:
                    answer = mid
                    end = mid - 1
                else:
                    start = mid + 1
            return 0 if answer == -1 else len(potions) - answer

        return [get_answer(spell) for spell in spells]