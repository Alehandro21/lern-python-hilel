fruits = ["яблоко", "банан", "апельсин"]
for fruit in fruits:
    print(fruit)
#выше это перебр данных путём использования цикла for
#ниже это тот же принцип интерации(перебора данных) только через цикл while
fruits = ["яблоко", "банан", "апельсин"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1