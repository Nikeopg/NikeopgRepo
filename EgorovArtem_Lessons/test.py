

with open("easy_passwords.txt", "r", encoding="utf-8") as file:
    x = [i for i in file.read().split()]
print(x)