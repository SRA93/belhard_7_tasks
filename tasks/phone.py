"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""


class Phone:
    brand = str
    model = str
    issue_year = int

    def __init__(self, brand: str, model: str, issue_year: int):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def __str__(self):
        return (f'Бренд: {self.brand}\n'
                f'Модель: {self.model}\n'
                f'Год выпуска: {self.issue_year}')

    def get_info(self):
        return self.brand, self.model, self.issue_year

    @staticmethod
    def receive_call(name: str):
        print(f'Звонит {name}')


mob_phone = Phone('iFruit', '5', 2013)

print(mob_phone)
mob_phone.receive_call('Майк')
print(mob_phone.get_info())
