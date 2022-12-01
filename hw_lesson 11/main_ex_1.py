"""
Реализуйте класс Блюдо, описывающее количество, название, стоимость и массу блюда.
Далее создайте несколько инстансов этого класса с описанием блюд.
Реализуйте класс Заказ, в инстанс которого можно было бы добавлять блюда.
Заказ должен содержать вычисляемые свойства: количество, стоимость, масса блюд в заказе.
Также реализуйте дополнительный метод "оплатить" (внесение определенной суммы в счет оплаты заказа)
и дополнительное свойство, обозначающее сумму, которую осталось оплатить
(с учетом стоимости заказа и внесенных с помощью метода «оплатить» денег)
"""

from dataclasses import dataclass


@dataclass
class Dish:
    count: int = 1
    name: str = 'Unknown'
    price: float = 1.0  # price in dollars for one dish
    weight: int = 1  # weight in grams for one dish


class Order:
    def __init__(self) -> None:
        print('--------New Order---------')
        self.order = []
        self.__amount = 0
        self.__price = 0
        self.__weight = 0
        self.__cash = 0
        self.__cash_for_pay = 0

    def add_dish(self, dish) -> None:
        self.order.append(dish)

    @property
    def amount(self):
        for i in self.order:
            self.__amount += i.count
        return self.__amount

    @property
    def price(self):
        for i in self.order:
            self.__price += i.price * i.count
        return self.__price

    @property
    def weight(self):
        for i in self.order:
            self.__weight += i.weight * i.count
        return self.__weight

    def pay(self,  cash: int = 0):
        self.__cash += cash

    @property
    def cash(self):
        self.__cash_for_pay = self.__price - self.__cash
        return self.__price - self.__cash


first_dish = Dish(1, 'Olivie', 2, 220)
second_dish = Dish(2, 'Pasta', 7, 280)
third_dish = Dish(2, 'Napoleon', 3, 200)

order1 = Order()
order1.add_dish(first_dish)
order1.add_dish(second_dish)
print(f'Количество всех заказанных блюд: {order1.amount}')
print(f'Стоимость, необходимую заплатить за заказ: {order1.price}$')
print(f'Суммарный вес всех блюд в заказе: {order1.weight} grams')
order1.pay(10)
print(f'Сумма, которую еще необходимо доплатить: {order1.cash}$')

order2 = Order()
order2.add_dish(first_dish)
order2.add_dish(second_dish)
order2.add_dish(third_dish)
print(f'Количество всех заказанных блюд: {order2.amount}')
print(f'Стоимость, необходимую заплатить за заказ: {order2.price}$')
print(f'Суммарный вес всех блюд в заказе: {order2.weight} grams')
order2.pay(15)
print(f'Сумма, которую еще необходимо доплатить: {order2.cash}$')
order2.pay(7)
print(f'Сумма, которую еще необходимо доплатить: {order2.cash}$')
