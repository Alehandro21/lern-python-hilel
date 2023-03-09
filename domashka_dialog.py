x = '>Hello, my name is Sasha, I like to play PS5! And what is your favorite activity?'
print(x)
x = (x.lower())
import re
x: str = re.sub(r'[^\w\s]', '', x)

input("What do you want to replace?\n> PS5")
position = x.find("PS5")
print(f"'PS5' was found at position {position}")


