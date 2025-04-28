import unittest
import json
import os

from src.base_file_handler import FileHandler


class MockFileHandler(FileHandler):
    """Конкретная реализация абстрактного класса FileHandler для тестирования."""

    def __init__(self, filename):
        self.filename = filename
        self.vacancies = []

    def load_vacancies_to_file(self, vacancies: list) -> None:
        """Метод для заполнения вакансиями полученными из hh.ru JSON-файла"""
        self.vacancies.extend(vacancies)
        with open(self.filename, 'w') as fl:
            json.dump(self.vacancies, fl)

    def add_vacancy(self, vacancy: dict) -> None:
        """Метод для добавления вакансии в файл"""
        self.vacancies.append(vacancy)
        with open(self.filename, 'w') as fl:
            json.dump(self.vacancies, fl)

    def get_vacancies(self, query: str) -> list[dict]:
        """Метод для получения вакансий из файла по запросу в описании"""
        return [vacancy for vacancy in self.vacancies if query in vacancy.get('description', '')]

    def delete_vacancy(self, vacancy_id: int) -> None:
        """Метод для удаления вакансии по ее id"""
        self.vacancies = [vacancy for vacancy in self.vacancies if vacancy.get('id') != vacancy_id]
        with open(self.filename, 'w') as fl:
            json.dump(self.vacancies, fl)


class TestFileHandler(unittest.TestCase):

    def setUp(self):
        """Метод подготовки окружения для тестов"""
        self.filename = 'test_vacancies.json'
        self.handler = MockFileHandler(self.filename)

    def tearDown(self):
        """Метод очистки после выполнения тестов"""
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_load_vacancies_to_file(self):
        """Тестируем загрузку выборки из API в файл"""
        vacancies = [{'id': 1, 'name': 'Developer'}, {'id': 2, 'name': 'Tester'}]
        self.handler.load_vacancies_to_file(vacancies)

        with open(self.filename, 'r') as fl:
            loaded_vacancies = json.load(fl)

        self.assertEqual(loaded_vacancies, vacancies)

    def test_add_vacancy(self):
        """Тестируем добавление вакансии в файл"""
        vacancy = {'id': 3, 'name': 'Manager'}
        self.handler.add_vacancy(vacancy)

        self.assertEqual(self.handler.vacancies, [vacancy])

    def test_get_vacancies(self):
        """Тестируем получение вакансий из файла по запросу в описании"""
        vacancies = [{'id': 1, 'description': 'Developer'}, {'id': 2, 'description': 'Tester'}]
        self.handler.load_vacancies_to_file(vacancies)

        result = self.handler.get_vacancies('Developer')

        self.assertEqual(result, [{'id': 1, 'description': 'Developer'}])

    def test_delete_vacancy(self):
        """Тестируем удаление вакансии по ее id"""
        vacancies = [{'id': 1, 'name': 'Developer'}, {'id': 2, 'name': 'Tester'}]
        self.handler.load_vacancies_to_file(vacancies)

        self.handler.delete_vacancy(1)

        result = self.handler.get_vacancies('')
        self.assertEqual(result, [{'id': 2, 'name': 'Tester'}])
