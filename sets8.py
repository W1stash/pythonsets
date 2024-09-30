lst = [1, 2, 4, 5, 7, 8]
p = lst[-1]

checker = []

for i in range(p):
    checker += [i+1]

s = set(checker).difference(set(lst))
print(s)
