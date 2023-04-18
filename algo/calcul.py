""" Boucle à travers les élements i de la liste trié en sens décroissant et 
    cherche les couples (peut être plus que 2 nombres) possibles telles 
    que i + x = n le nombre recherché. Ensuite vérifie si le couple 
    y + z = x (y et z appartenant a la liste) existe récursivement 
    jusqu'à ce que soit le couple existe, soit couple impossible."""
def main(card: dict) -> str:
    nums = card.get("numbers")
    nums.sort(reverse=True)
    n = card.get("result")
    possible = []
    # boucle à travers élements liste nums et ajoute dans couple possibles
    for i in range(len(nums)):
        if nums[i] < n:
            possible.append([i+1, n - nums[i], nums[i]])
        elif nums[i] == n:
            return nums[i]
    # jusqu'à ce qu'il existe un couple possible, vérifie si ils existent 
    # ou si ils peuvent être formés d'autres couples
    while possible != []: 
        buffer=[]
        for j in possible:
            for i in range(j[0],len(nums)):
                if  0 <= j[1] - nums[i] <= nums[i]:
                    if j[1] == nums[i] :
                        return("+".join(str(i) for i in [nums[i]] + j[2:]))
                    else:
                        buffer.append([i+1, j[1] - nums[i], nums[i]] + j[2:])
        possible=buffer