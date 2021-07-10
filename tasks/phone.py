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

    @classmethod
    def receive_call(cls, name="Анатолий"):
        cls.name = name
        print(f"Звонит: {cls.name}")

    def get_info(self):
        print(self.brand, self.model, self.issue_year)

    def __str__(self):
        return f"<Бренд: {self.brand}, Модель: {self.model}, Год выпуска: {self.issue_year}>"


mob_phones = Phone

mob_phones = [
    ['iFruit', '10', 2019],
    ['Xiaix', 'dmi7', 2018],
    ['Gnusmas', 'a12', 2020]
]

print(mob_phones)
Phone.receive_call()
