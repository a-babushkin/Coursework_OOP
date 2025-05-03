import unittest

from src.base_external_api import JobWithAPI


class MockJobWithAPI(JobWithAPI):
    """Фейковая реализация JobWithAPI для тестирования."""

    def _connect(self) -> None:
        """Имитация соединения с API."""
        self.connected = True

    def get_vacancies(self, query: str, pages: int) -> list:
        """Возвращает имитированные вакансии по запросу."""
        if not self.connected:
            raise ConnectionError("Не установлено соединение с API.")

        return [
            {"id": 1, "name": "Developer", "description": "Разработчик ПО"},
            {"id": 2, "name": "Tester", "description": "Тестировщик ПО"},
        ]


class TestJobWithAPI(unittest.TestCase):

    def setUp(self) -> None:
        """Подготовка тестов."""
        self.api = MockJobWithAPI()
        self.api._connect()

    def test_connection(self) -> None:
        """Тестируем установление соединения."""
        self.assertTrue(hasattr(self.api, "connected"))
        self.assertTrue(self.api.connected)

    def test_get_vacancies(self) -> None:
        """Тестируем получение вакансий по запросу."""
        vacancies = self.api.get_vacancies("Developer", 1)

        self.assertIsInstance(vacancies, list)
        self.assertGreater(len(vacancies), 0)
        self.assertEqual(vacancies[0]["name"], "Developer")

    def test_no_connection(self) -> None:
        """Тестируем, что вызов get_vacancies без соединения вызывает ошибку."""
        api_without_connection = MockJobWithAPI()
        api_without_connection.connected = False
        with self.assertRaises(ConnectionError):
            api_without_connection.get_vacancies("Developer", 1)
