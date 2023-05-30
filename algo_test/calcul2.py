""" Boucle à travers les élements de la liste triés en sens décroissant et cherche les couples possibles.
    Vérifient si ces couples existent récursivement
    !!!Version actuel calcul toutes les couples avant de retourner un couple, dans version finale retourner dès que couple trouvé!!"""
def main(card: dict) -> str:
    nums = card.get("numbers")
    nums.sort(reverse=True)
    n = card.get("result")
    possible=[]
    for i in range(len(nums)): #boucle à travers élements liste nums et ajoute dans possible couple possibles
        if nums[i] < n:
            possible.append([i+1, n - nums[i], [nums[i]]])
        elif nums[i] == n:
            return str(nums[i])
    while possible != []: #tant qu'il existe des couples possibles, vérifie si ils existent ou si ils peuvent être formés d'autres couples
        buffer=[]
        for j in possible:
            for i in range(j[0],len(nums)):
                rest = j[1]
                nu = nums[i]
                if  0 <= j[1] - nu <= n:
                    if j[1] == nu :
                        return "+".join(str(i) for i in [nu] + j[2])
                    else:
                        buffer.append([i+1, j[1] - nu, j[2] + [nu]])
        possible=buffer 