import re # добавляем библиотеку для: убираем всё лишнее кроме букв

print("Please, input your string:") #выводим первое отображаемое сообщение которое видим в консоли

str = input() #первая переменная
str = str.lower() #переводим всё в нижний регистр
str = re.sub(r'[^\w\s]', '', str) #убираем всё лишнее кроме букв
str = str.rstrip() #убираем лишние пробелы и табуляции


print("What do you want to replace?") #второе отображаемое сообщение в консоли от имени программы
str_to_replace = input() #строка которую хотим заменить

index_of_str_to_replace = str.find(str_to_replace) #позволит найти искомое слово, и как следствие заменить его на новое

print(f'"{str_to_replace}" was found at position {index_of_str_to_replace}!')
print("With what do you want to replace?")

new_str = input() #строка, на которую мы будем заменять

result = re.sub(str_to_replace, new_str, str) # то что нужно поменять, то на что нужно поменять и где это нужно сделать

print(f'Here is your result: {result}') #вуаля, получили даилог с программой




#x = input()
#x = (x.lower())
#x: str = re.sub(r'[^\w\s]', '', x)
#
#print("What do you want to replace?")
#
#str_for_replace_from = input() #снова ожидаем ввод текста
#str_for_replace_to = input() #снова ожидаем ввод текста
#
#x = re.sub(str_for_replace_from, str_for_replace_to, x)
#
#print("result is - \n " + x)

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