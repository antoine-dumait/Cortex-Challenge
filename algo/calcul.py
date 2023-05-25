from itertools import combinations
def main(card :dict) -> str:
    nums = card.get("numbers")
    nums.sort()
    n = card.get("result")
    for m in range(1, len(nums)+1):
        for combination in combinations(nums , m): 
            if sum(combination) == n:
                return '+'.join(str(num) for num in combination) #already sorted