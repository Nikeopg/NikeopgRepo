class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f"Пользователь {self.login}, баланс - {self.balance}"

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.__balance += value

    def payment(self, pay):
        if pay > self.__balance:
            print("Не хватает средств на балансе. Пополните счет")
            return False
        else:
            self.__balance = self.__balance - pay
            return True


class Cart:
    def __init__(self, user: User):
        self.user = user
        self.goods = {}
        self.__total = 0

    def add(self, Prod, amount=1):
        self.goods[Prod] = self.goods.get(Prod, 0) + amount
        self.__total = self.__total + (amount * Prod.price)

    def remove(self, Prod, amount=1):
        if amount >= self.goods[Prod]:
            amount = self.goods[Prod]
            self.goods[Prod] = self.goods.get(Prod, 0) - amount
            self.__total -= amount * Prod.price

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.total):
            print("Заказ оплачен")
        else:
            print("Проблема с оплатой")

    def print_check(self):
        print(f"---Your check---")
        for k,v in sorted(self.goods.items(), key = lambda x: x[0].name):
            if v > 0:
                print(f"{k.name} {k.price} {v} {k.price * v}")
            else:
                pass
        print(f"---Total: {self.total}---")

billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)

print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20

"""
Все вы думаю сталкивались с оформлением заказов в онлайн магазинах. Давайте и мы воссоздадим этот процесс
Часть 1
Для этого нам понадобится реализовать несколько классов и связать их между собой. Первый класс, который мы реализуем, будет Product. Это класс, описывающий товар. В нем должно быть реализовано:

метод __init__, принимающий на вход имя товара и его стоимость. Эти значения необходимо сохранить в атрибутах name и price  
Пример работы с классом Product

carrot = Product('carrot', 30)
print(carrot.name, carrot.price)
____________________________
Часть 2
Далее для оформления заказа нам нужен пользователь. Для этого создадим класс User, который содержит:

метод __init__, принимающий на вход логин пользователя и необязательный аргумент баланс его счета(по умолчанию 0). Логин необходимо сохранить в атрибуте login , а баланс необходимо присвоить сеттеру   balance  (см. пункт 4)
метод __str__, возвращающий строку вида «Пользователь {login}, баланс - {balance}»
Cвойство геттер balance, которое возвращает значение self.__balance;
Свойство сеттер balance, принимает новое значение баланса и устанавливает его в атрибут self.__balance ;
метод deposit  принимает числовое значение и прибавляет его к атрибуту self.__balance ;
метод payment  принимает числовое значение, которое должно списаться с баланса пользователя. Если на счете у пользователя не хватает средств, то необходимо вывести фразу  «Не хватает средств на балансе. Пополните счет» и вернуть False. Если средств хватает, списываем с баланса у пользователя указанную сумму и возвращаем True
Пример работы с классом User

billy = User('billy@rambler.ru')
print(billy) # Пользователь billy@rambler.ru, баланс - 0
billy.deposit(100)
billy.deposit(300)
print(billy) # Пользователь billy@rambler.ru, баланс - 400
billy.payment(500) # Не хватает средств на балансе. Пополните счет
billy.payment(150)
print(billy) # Пользователь billy@rambler.ru, баланс - 250
Необходимо только написать определение класса User
"""
