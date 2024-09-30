text1 = "The quick brown fox jumps over the lazy dog".lower()
text2 = "The slow turtle jumps under the energetic dog".lower()

array1 = text1.split(" ")
array2 = text2.split(" ")

t1u = set(array1).difference(set(array2))
t2u = set(array2).difference(set(array1))
c = set(array1).intersection(set(array2))

print(t1u, t2u, c)


