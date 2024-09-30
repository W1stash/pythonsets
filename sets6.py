youtube = {"Albert", "Bob", "John"}
yandex = {"Alex", "Bob", "Mike"}
vk = {"Mike", "Bob", "Marshall"}

users1 = []
users3 = []

s = youtube.union(yandex.union(vk))
f = list(youtube) + list(yandex) + list(vk)

for elements in s:
    i = 0
    for elementf in f:
        if elements == elementf:
            i += 1
    if i == 1:
        users1 += [elements]
    elif i == 3:
        users3 += [elements]

print(s)
print(f)
print("")
print(users1)
print(users3)

# Почему-то я сразу не додумался, что можно решить намного быстрее
# С помощью difference() и intersection()
            
        
