"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n
- метод generate, который принимает длину последовательности n
- метод print_seq, который выводит последовательность на экран
"""


class RandSequence:
    sequence = []

    def __init__(self, sequence):
        self.sequence = sequence

    def generate(self):
        len(self.sequence)

    def __repr__(self):
        return f"Последовательность = {self.sequence}"

    def print_seq(self):
        return self.sequence


numbers = RandSequence([1, 4, 656, 343, 9, 6, 645])
print(numbers)
