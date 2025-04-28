from unittest import TestCase

from src.vacancies import Vacancy


class TestVacancy(TestCase):

    def setUp(self):
        """Подготовка к тестам."""
        self.vacancy_1 = Vacancy('Developer', 'Company A', {'from': 60000, 'to': 80000}, 'https://example.com',
                                 'Разработчик ПО')
        self.vacancy_2 = Vacancy('Tester', 'Company B', {'from': 40000, 'to': 60000}, 'https://example.com',
                                 'Тестировщик ПО')

    def test_initialization(self):
        """Тестируем инициализацию вакансии."""
        self.assertEqual(self.vacancy_1.name, 'Developer')
        self.assertEqual(self.vacancy_1.company, 'Company A')
        self.assertEqual(self.vacancy_1.salary, 70000)  # (60000 + 80000) / 2
        self.assertEqual(self.vacancy_1.url, 'https://example.com')
        self.assertEqual(self.vacancy_1.description, 'Разработчик ПО')

    def test_salary_setter(self):
        """Тестируем setter для зарплаты."""
        self.vacancy_2.salary = {'from': 30000, 'to': 50000}
        self.assertEqual(self.vacancy_2.salary, 40000)  # (30000 + 50000) / 2

        self.vacancy_2.salary = {'from': 0, 'to': 30000}
        self.assertEqual(self.vacancy_2.salary, 30000)

        self.vacancy_2.salary = {'from': 30000, 'to': 0}
        self.assertEqual(self.vacancy_2.salary, 30000)

        self.vacancy_2.salary = {'from': None, 'to': None}
        self.assertEqual(self.vacancy_2.salary, 0)

    def test_name_setter(self):
        """Тестируем setter для названия вакансии."""
        self.vacancy_1.name = []
        self.assertEqual(self.vacancy_1.name, "Название отсутствует")

        self.vacancy_1.name = None
        self.assertEqual(self.vacancy_1.name, "Название отсутствует")

    def test_company_setter(self):
        """Тестируем setter для названия компании."""
        self.vacancy_1.company = []
        self.assertEqual(self.vacancy_1.company, "Название работодателя отсутствует")

        self.vacancy_1.company = None
        self.assertEqual(self.vacancy_1.company, "Название работодателя отсутствует")

    def test_url_setter(self):
        """Тестируем setter для URL вакансии."""
        self.vacancy_1.url = 'invalid_url'
        self.assertEqual(self.vacancy_1.url, "Ссылка отсутствует")

    def test_description_setter(self):
        """Тестируем setter для описания вакансии."""
        self.vacancy_1.description = 12345
        self.assertEqual(self.vacancy_1.description, "Описание отсутствует")

    def test_comparison_operators(self):
        """Тестируем операторы сравнения."""
        self.assertTrue(self.vacancy_1 > self.vacancy_2)  # 70000 > 40000
        self.assertTrue(self.vacancy_1 >= self.vacancy_1)  # 70000 >= 70000
        self.assertTrue(self.vacancy_2 < self.vacancy_1)  # 40000 < 70000

    def test_to_dict(self):
        """Тестируем метод to_dict."""
        expected_dict = {
            'id': self.vacancy_1.id,
            'name': 'Developer',
            'company': 'Company A',
            'salary': 70000,
            'url': 'https://example.com',
            'description': 'Разработчик ПО'
        }
        self.assertEqual(self.vacancy_1.to_dict(), expected_dict)

    def test_vacancy_str(self):
        """Тестирует метод __str__ ."""
        expected_string = ("Вакансия(id='1', название='Developer', работодатель='Company A', зарплата=70000, "
                           "ссылка='https://example.com', описание='Разработчик ПО')")
        self.vacancy_1.id = 1
        self.assertEqual(str(self.vacancy_1), expected_string)
