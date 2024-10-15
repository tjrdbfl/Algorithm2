import itertools as itt

print("permutations: ") # 순열
for perm in itt.permutations(range(4),2):
    print(perm)

print("product: ")  # 중복 순열
for prod in itt.product(range(4),repeat=10):
    print(prod)

print("combinations: ") # 조합
for comb in itt.combinations(range(4),2):
    print(comb)

print("combinations_with_replacement: ") # 중복 조합
for comb in itt.combinations_with_replacement(range(4),2):
    print(comb)