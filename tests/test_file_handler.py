import json
import os
from unittest import mock, TestCase
from src.file_handler import JSONFileHandler


class TestJSONFileHandler(TestCase):

    def setUp(self):
        """Подготовка к тестам."""
        self.test_file_path = 'test_vacancies.json'  # Путь к тестовому файлу
        self.handler = JSONFileHandler(self.test_file_path)

    def tearDown(self):
        """Очистка после тестов."""
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_load_vacancies_to_file(self):
        """Тестируем загрузку вакансий в файл."""
        vacancies = [{'id': 1, 'name': 'Developer', 'description': 'Разработчик ПО'}]
        self.handler.load_vacancies_to_file(vacancies)

        with open(self.test_file_path, 'r', encoding='utf-8') as f:
            loaded_vacancies = json.load(f)

        self.assertEqual(loaded_vacancies, vacancies)

    def test_add_vacancy(self):
        """Тестируем добавление вакансии."""
        vacancy1 = {'id': 1, 'name': 'Developer', 'description': 'Разработчик ПО'}
        vacancy2 = {'id': 2, 'name': 'Tester', 'description': 'Тестировщик ПО'}

        self.handler.load_vacancies_to_file([vacancy1])
        self.handler.add_vacancy(vacancy2)

        with open(self.test_file_path, 'r', encoding='utf-8') as f:
            vacancies = json.load(f)

        self.assertEqual(len(vacancies), 2)
        self.assertIn(vacancy2, vacancies)

    def test_get_vacancies(self):
        """Тестируем получение вакансий по запросу."""
        vacancies = [
            {'id': 1, 'name': 'Developer', 'description': 'Разработчик ПО'},
            {'id': 2, 'name': 'Tester', 'description': 'Тестировщик ПО'}
        ]
        self.handler.load_vacancies_to_file(vacancies)

        result = self.handler.get_vacancies('Разработчик')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], 1)

    def test_delete_vacancy(self):
        """Тестируем удаление вакансии."""
        vacancies = [{'id': 1, 'name': 'Developer', 'description': 'Разработчик ПО'}]
        self.handler.load_vacancies_to_file(vacancies)
        self.handler.delete_vacancy(1)

        with open(self.test_file_path, 'r', encoding='utf-8') as f:
            remaining_vacancies = json.load(f)

        self.assertEqual(len(remaining_vacancies), 0)
