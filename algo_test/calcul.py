import itertools
def main(card :dict) -> str:
    nums = card.get("numbers")
    nums.sort(reverse=True)
    n = card.get("result")
    for m in range(1, len(nums)+1):
        for combination in itertools.combinations(nums , m):
            if sum(combination) == n:
                return '+'.join(str(num) for num in sorted(combination))
    return "Aucune combinaison trouvée"