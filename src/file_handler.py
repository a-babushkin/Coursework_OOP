import json
import os
from typing import Any

from src.base_file_handler import FileHandler


class JSONFileHandler(FileHandler):
    """Класс для работы с вакансиями в JSON-файле"""

    def __init__(self, path_to_file: str = "data/vacancies.json") -> None:
        self.path_to_file = path_to_file

    def load_vacancies_to_file(self, vacancies: list) -> None:
        """Метод для заполнения вакансиями полученными из hh.ru JSON-файла"""
        if vacancies:
            with open(self.path_to_file, mode='w', encoding="UTF-8") as fl:
                json.dump(vacancies, fl, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: dict) -> None:
        """Метод для добавления вакансии в файл"""
        vacancies = self.get_vacancies()
        if vacancy not in vacancies:
            vacancies.append(vacancy)
            with open(self.path_to_file, mode='w', encoding="UTF-8") as fl:
                json.dump(vacancies, fl, ensure_ascii=False, indent=4)

    def get_vacancies(self, query: str = '') -> Any:
        """Метод для получения вакансии из файла по запросу в описании"""
        if not os.path.exists(self.path_to_file):
            return []
        with open(self.path_to_file, mode='r', encoding='UTF-8') as file:
            vacancies = json.load(file)
        if query:
            filtered_vacancies = []
            for vacancy in vacancies:
                if query in vacancy.get('description'):
                    filtered_vacancies.append(vacancy)
            return filtered_vacancies
        return vacancies

    def delete_vacancy(self, vacancy_id: int) -> None:
        """Метод для удаления вакансии по ее id"""
        vacancies = self.get_vacancies()
        vacancies = [vacancy for vacancy in vacancies if vacancy.get('id') != vacancy_id]
        with open(self.path_to_file, 'w') as f:
            json.dump(vacancies, f, indent=4)
