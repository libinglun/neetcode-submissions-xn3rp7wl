class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = defaultdict(int)
        for num in hand:
            count[num] += 1

        hand.sort()
        for num in hand:
            # starts from the minimum, the second left one is the second start value
            if count[num]:
                # find all the members incremented from the start
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1

        return True

        
