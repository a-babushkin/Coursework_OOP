from abc import ABC, abstractmethod


class FileHandler(ABC):
    """Абстрактный класс для обработки файлов с вакансиями"""

    @abstractmethod
    def load_vacancies_to_file(self, vacancies: list) -> None:
        """Метод для заполнения вакансиями полученными из hh.ru JSON-файла"""
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: dict) -> None:
        """Абстрактный метод для добавления вакансии в файл"""
        pass

    @abstractmethod
    def get_vacancies(self, query: str) -> list[dict]:
        """Абстрактный метод для получения вакансии из файла по запросу"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id: int) -> None:
        """Абстрактный метод для удаления вакансии из файла по идентификатору"""
        pass
