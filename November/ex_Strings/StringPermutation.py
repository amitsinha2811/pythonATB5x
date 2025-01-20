from itertools import permutations

def find_permutation(s:str) -> list:
    return [''.join(p) for p in permutations(s)]

print(find_permutation("ABC"))