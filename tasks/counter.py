"""
Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты:

- value - текущее значение счетчика

Определить методы:

- инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
- increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
- decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
- метод __iter__
- метод __next__
"""


class Counter:
    value = 0

    def __init__(self, start=None, end=None):

        self.start = start
        self.end = end

    def increase(self):
        if self.value < self.end:
            self.value += 1
            return self.value
        else:
            return 'Вне диапазона'

    def decrease(self):
        if self.value < self.end:
            self.value -= 1
            return self.value
        else:
            return 'Вне диапазона'

    def __iter__(self):
        return self

    def __next__(self):
        value = self.value
        if self.value <= self.end:
            self.value += 1
            return value
        else:
            raise StopIteration


count_next = Counter(start=0, end=20)


print(count_next.increase())
print(count_next.increase())
print(count_next.increase())
print(count_next.increase())
print(count_next.increase())
print(count_next.increase())
