# первая часть домашки

string = input("Введите строку:")
string = string.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("_", "")\
    .lower()#занижаем, убираем всё лишнее
if string == string[::-1]:  # проверяем, является ли строка зеркальной
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")

# вторая часть домашки

text = input("Валяй: ")
left_bracket = text.find("(")
right_bracket = text.find(")")

# Если найдены обе скобки, удалить все между ними
if left_bracket != -1 and right_bracket != -1:
    output_str = text[:left_bracket] + text[right_bracket+1:]
else:
    output_str = text

print(output_str)

