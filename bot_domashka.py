while True:
    user_input = input("Ви: ")
    user_input = user_input.lower() # Преобразование введенной строки в нижний регистр
    if "привіт" in user_input or "хай" in user_input or "доброго дня" in user_input:
        print("Бот: Доброго вечора, я бот з України!")
    elif "як справи?" in user_input or "що робиш?" in user_input or "чим займаєшся?" in user_input:
        print("Бот: Вчусь програмувати на Python!")
    elif "фільм" in user_input or "кінотеатр" in user_input or "серіал" in user_input:
        print("Бот: Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться фільм Тор: Рагнарьок, він просто бомба!")
    elif "бувай" in user_input or "надобраніч" in user_input or "гудбай" in user_input or "до зустрічі" in user_input:
        print("Бот: Побачимось у мережі, I'll be back.")
        break
    else:
        print("Бот: Дуже цікаво, але, нажаль, нічого не зрозуміло :(")