"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:

    surname: str
    name: str
    group: int
    average_score: float

    def __init__(self, surname: str, name: str, group: int, average_score: float):

        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __lt__(self, other):
        return self.average_score < other.average_score

    def __gt__(self, other):
        return self.average_score > other.average_score

    def __ne__(self, other):
        return self.average_score != other.average_score

    def __le__(self, other):
        return self.average_score <= other.average_score

    def __ge__(self, other):
        return self.average_score >= other.average_score

    def __repr__(self):
        return f"<Фамилия= {self.surname}, Имя= {self.name}, Группа= {self.group}, Балл= {self.average_score}>"


stud_list = Student

stud_list = [
    ['Фамилия1', 'Студент1', 234, 3.7],
    ['Фамилия2', 'Студент2', 235, 7.4],
    ['Фамилия3', 'Студент3', 234, 9.1],
    ['Фамилия4', 'Студент4', 233, 6.0],
    ['Фамилия5', 'Студент5', 235, 5.2]
]

print(sorted(stud_list))
print(sorted(stud_list, reverse=True))
print(list(filter(lambda x: x[-1] >= 5, stud_list)))
