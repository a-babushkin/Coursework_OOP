class Vacancy:
    """Класс для работы с вакансиями."""

    __slots__ = ('id', '_name', '_company', '_salary', '_url', '_description')

    vacancy_id = 1

    def __init__(self, name: str, company: str, salary: dict, url: str, description: str) -> None:
        self.id = Vacancy.vacancy_id
        self.name = name
        self.company = company
        self.salary = salary
        self.url = url
        self.description = description
        Vacancy.vacancy_id += 1

    # ===========Группа методов setters & getters атрибутов вакансий============

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Метод setter с валидацией названия вакансии"""
        if isinstance(name, str) or name:
            self._name = name
        else:
            self._name = "Название отсутствует"

    @property
    def company(self) -> str:
        return self._company

    @company.setter
    def company(self, company: str) -> None:
        """Метод setter с валидацией работодателя"""
        if isinstance(company, str) or company:
            self._company = company
        else:
            self._company = "Название работодателя отсутствует"

    @property
    def salary(self) -> int:
        return self._salary

    @salary.setter
    def salary(self, salary: dict) -> None:
        """Метод setter с валидацией суммы заработной платы"""
        local_salary_from = 0
        local_salary_to = 0

        if isinstance(salary, dict):
            if isinstance(salary.get('from'), (int, float)):
                local_salary_from = salary.get('from', 0)

            if isinstance(salary.get('to'), (int, float)):
                local_salary_to = salary.get('to', 0)

        if local_salary_from > 0 and local_salary_to > 0:
            self._salary = round((local_salary_from + local_salary_to) / 2)
        elif local_salary_from == 0:
            self._salary = local_salary_to
        else:
            self._salary = local_salary_from

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, url: str) -> None:
        """Метод setter с валидацией ссылки на вакансию"""
        if isinstance(url, str) or url.startswith("http"):
            self._url = url
        else:
            self._url = "Ссылка отсутствует"

    @property
    def description(self) ->str:
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """Метод setter с валидацией описания вакансии"""
        if isinstance(description, str):
            self._description = description
        else:
            self._description = "Описание отсутствует"

    # ===========Группа магических методов сравнения вакансий============

    def __lt__(self, other: object):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary <= other.salary

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __ne__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary != other.salary

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary > other.salary

    def __ge__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary >= other.salary

    # ==============================================

    def __str__(self) -> str:
        return (f"Вакансия(id='{self.id}', название='{self.name}', работодатель='{self.company}', "
                f"зарплата={self.salary}, ссылка='{self.url}', описание='{self.description}')")

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'company': self.company,
            'salary': self.salary,
            'url': self.url,
            'description': self.description
        }

# if __name__ == '__main__':
#     v1 = Vacancy('worker', 'BMV', {
#         "from": 130000,
#         "to": None,
#     }, 'https://', '12')
#     v2 = Vacancy('coworker', 'Audi', {
#         "from": 570000,
#         "to": None,
#     }, 'https://', '13')
#     v3 = Vacancy('engineer', 'BMV', {
#         "from": 7000,
#         "to": 90000,
#     }, 'https://', '14')
#     _list = [v1, v2, v3]
#     # print(_list)
#     [print(v) for v in sorted(_list, reverse=True)]
# for v in _list:
#     print(v)
# print(
#     f"Вакансия(id='{v.id}', название='{v.name}', работодатель='{v.company}', зарплата={v.salary}, ссылка='{v._url}', описание='{v._description}')")
