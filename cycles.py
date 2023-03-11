total = 0
while True:
    user_input = input("Введите число: ")
    if user_input == "sum":
        break
    elif (user_input[0] == '-' and user_input[1:].isnumeric()) or (user_input.isnumeric()) \
            or (user_input.count('.') == 1 and user_input.replace('.', '').isnumeric()):
        number = float(user_input)
        total += number
    else:
        print("Некорректный ввод. Пожалуйста введите число!")
print(total)
