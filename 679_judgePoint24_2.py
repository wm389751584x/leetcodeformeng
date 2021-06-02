from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        def helper(cards):
            size = len(cards)

            if size == 1:
                return abs(cards[0] - 24) < 0.1

            for i, x in enumerate(cards):
                for j, y in enumerate(cards):
                    if i == j:
                        continue
                    combo = []
                    combo.append(x+y)
                    combo.append(x-y)
                    combo.append(x*y)
                    if y:
                        combo.append(x/y)
                    remain = [cards[_] for _ in range(size) if _ not in [i, j]]
                    for card in combo:
                        if helper(remain + [card]):
                            return True

        return True if helper(cards) else False


if __name__ == "__main__":
    S = Solution()
    assert S.judgePoint24([1,2,1,2]) == False
    assert S.judgePoint24([4,1,8,7]) == True