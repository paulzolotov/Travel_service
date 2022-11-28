"""
3. Реализуйте класс Counter, который дополнительно принимает начальное значение и конечное значение счетчика.
Если начальное значение не указано, счетчик должен начинаться с 0. Если стоп-значение не указано, оно должно
считаться вверх бесконечно. Если счетчик достигает стоп-значения, выведите «Maximal value is reached».
Реализовать методы: "increment" (увеличивает счетчик на 1) и "get" (выводит информацию о значении счетчика)
Пример:
c = Counter(start=42)
c.increment()
c.get()
43

c = Counter()
c.increment()
c.get()
1
c.increment()
c.get()
2

c = Counter(start=42, stop=43)
c.increment()
c.get()
43
c.increment()
Maximal value is reached.
c.get()
43
"""


class Counter:

    def __init__(self, start: int = 0, stop: int = float('inf')):
        self.start = start
        self.stop = stop
        self.value = start

    def increment(self):
        if self.value >= self.stop:
            print('Maximal value is reached')
        else:
            self.value += 1

    def get(self):
        return self.value


c = Counter(start=42)
c.increment()
print(c.get())  # 43

c = Counter()
c.increment()
print(c.get())  # 1
c.increment()
print(c.get())  # 2

c = Counter(start=42, stop=43)
c.increment()
print(c.get())  # 43
c.increment()  # Maximal value is reached.
print(c.get())  # 43
