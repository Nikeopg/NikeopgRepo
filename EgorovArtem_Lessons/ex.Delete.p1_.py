class File:
    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f"Файл {self.name} восстановлен из корзины")
        self.in_trash = False

    def remove(self):
        print(f"Файл {self.name} был удален")
        self.is_deleted = True

    def read(self):
        if self.is_deleted:
            return print(f"ErrorReadFileDeleted({self.name})")
        if self.in_trash:
            return print(f"ErrorReadFileTrashed({self.name})")
        else:
            return print(f"Прочитали все содержимое файла {self.name}")

    def write(self, content):
        if self.is_deleted:
            return print(f"ErrorWriteFileDeleted({self.name})")
        if self.in_trash:
            return print(f"ErrorWriteFileTrashed({self.name})")
        else:
            return print(f"Записали значение {content} в файл {self.name}")


class Trash:
    content = []

    @staticmethod
    def add(value):
        if not isinstance(value, File):
            return print(f"В корзину добавлять можно только файл")
        else:
            Trash.content.append(value)
            value.in_trash = True

    @staticmethod
    def clear():
        print(f"Очищаем корзину")
        for i in Trash.content:
            File.remove(i)
        Trash.content.clear()
        print('Корзина пуста')

    @staticmethod
    def restore():
        print("Восстанавливаем файлы из корзины")
        for i in Trash.content:
            File.restore_from_trash(i)
        Trash.content.clear()
        print("Корзина пуста")

f1 = File('puppies.jpg')
f2 = File('cat.jpg')
passwords = File('pass.txt')

f1.read() # Прочитали все содержимое файла puppies.jpg
Trash.add(f1)
f1.read() # ErrorReadFileTrashed(puppies.jpg)

Trash.add(f2)
Trash.add(passwords)
Trash.clear() # после этой команды вывод должен быть таким
'''
Очищаем корзину
Файл puppies.jpg был удален
Файл cat.jpg был удален
Файл pass.txt был удален
Корзина пуста
'''

f1.read() # ErrorReadFileTrashed(puppies.jpg)




"""
Задача Корзина
Давайте реализуем ситуация создания файлов и перемещения их в корзину. Задача будет состоять из двух частей

Часть 1
Создайте класс  File, у которого есть:

метод __init__, который должен принимать на вход имя файла и записывать его в атрибут name. Также необходимо создать атрибуты in_trash , is_deleted  и записать в них значение False
метод  restore_from_trash, который печатает фразу «Файл {name} восстановлен из корзины» и проставляет атрибут in_trash в значение False
метод  remove, который печатает фразу «Файл {name} был удален» и проставляет атрибут is_deleted  в значение True
метод read, который
печатает фразу «ErrorReadFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
печатает фразу «ErrorReadFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
печатает фразу «Прочитали все содержимое файла {self.name}» если файл не удален и не в корзине
метод write, который принимает значение content для записи и
печатает фразу «ErrorWriteFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
печатает фразу «ErrorWriteFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
печатает фразу «Записали значение {content} в файл {self.name}», если файл не удален и не в корзине
Пример работы с классом File

f1 = File('puppies.jpg')
print(f1.__dict__)  # {'name': 'puppies.jpg', 'in_trash': False, 'is_deleted': False}
f1.read()  # Прочитали все содержимое файла puppies.jpg
f1.remove()  # Файл puppies.jpg был удален
f1.read()  # ErrorReadFileDeleted(puppies.jpg)

f2 = File('cat.jpg')
f2.write('hello')  # Записали значение hello в файл cat.jpg
f2.remove()  # Файл cat.jpg был удален
f2.write('world')  # ErrorWriteFileDeleted(cat.jpg)


Далее создайте класс  Trash у которого есть:

атрибут класса  content изначально равный пустому списку
статик-метод  add, который принимает файл и сохраняет его в корзину: для этого нужно добавить его в атрибут content и проставить файлу атрибут in_trash значение True. Если в метод add передается не экземпляр класса File, необходимо вывести сообщение «В корзину добавлять можно только файл»
статик-метод  clear, который запускает процесс очистки файлов в корзине. Необходимо для всех файлов, хранящийся в атрибуте content , в порядке их добавления в корзину вызвать метод файла remove. Атрибут content  после очистки должен стать пустым списком. Сама процедура очистки должна начинаться фразой «Очищаем корзину» и заканчиваться фразой «Корзина пуста»
статик-метод  restore, который запускает процесс восстановления файлов из корзины. Необходимо для всех файлов, хранящийся в атрибуте content , в порядке их добавления в корзину вызвать метод файла restore_from_trash. Атрибут content  после очистки должен стать пустым списком. Сама процедура восстановления должна начинаться фразой «Восстанавливаем файлы из корзины» и заканчиваться фразой «Корзина пуста»
"""
