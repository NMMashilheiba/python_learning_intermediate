from itertools import combinations, permutations, combinations_with_replacement
a = [1, 2, 3]

comb = combinations(a, 2)
perm_1 = permutations(a, 1)
comb_wr = combinations_with_replacement(a, 2)

print(list(comb))
print(list(perm_1))
print(list(comb_wr))

