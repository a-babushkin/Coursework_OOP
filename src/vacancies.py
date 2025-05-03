from typing import Any


class Vacancy:
    """Класс для работы с вакансиями."""

    __slots__ = ("id", "_name", "_company", "_salary", "_url", "_description")

    vacancy_id = 1

    def __init__(self, name: str, company: str, salary: Any, url: str, description: str) -> None:
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
        if isinstance(name, str) and name != "":
            self._name = name
        else:
            self._name = "Название отсутствует"

    @property
    def company(self) -> str:
        return self._company

    @company.setter
    def company(self, company: str) -> None:
        """Метод setter с валидацией работодателя"""
        if isinstance(company, str) and company != "":
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
            if isinstance(salary.get("from"), (int)):
                local_salary_from = salary.get("from", 0)

            if isinstance(salary.get("to"), (int)):
                local_salary_to = salary.get("to", 0)

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
        if isinstance(url, str) and url.startswith("http"):
            self._url = url
        else:
            self._url = "Ссылка отсутствует"

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """Метод setter с валидацией описания вакансии"""
        if isinstance(description, str) and description != "":
            self._description = description
        else:
            self._description = "Описание отсутствует"

    # ===========Группа магических методов сравнения вакансий============

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary <= other.salary

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary != other.salary

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary > other.salary

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary >= other.salary

    # ==============================================

    def __str__(self) -> str:
        return (
            f"Вакансия(id='{self.id}', название='{self.name}', работодатель='{self.company}', "
            f"зарплата={self.salary}, ссылка='{self.url}', описание='{self.description}')"
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "company": self.company,
            "salary": self.salary,
            "url": self.url,
            "description": self.description,
        }
