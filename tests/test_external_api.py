from unittest import TestCase
from unittest.mock import patch, MagicMock
from dotenv import load_dotenv

from src.external_api import HeadHunterAPI
from src.connect_api_exception import ConnectAPIError


class TestHeadHunterAPI(TestCase):

    def setUp(self):
        """Подготовка к тестам."""
        load_dotenv()
        self.hh_api = HeadHunterAPI()

    @patch('requests.get')
    def test_connect_success(self, mock_get):
        """Тест успешного соединения с API."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        self.hh_api._connect()

    @patch('requests.get')
    def test_connect_failure(self, mock_get):
        """Тест неуспешного соединения с API."""
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        with self.assertRaises(ConnectAPIError) as context:
            self.hh_api._connect()
        self.assertEqual(str(context.exception), "Соединение не установлено. Код ошибки: 500")

    @patch('requests.get')
    def test_get_vacancies_successful(self, mock_get):
        """Тестирование успешного получения вакансий."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'items': [{'id': 1, 'name': 'Vacancy 1'}, {'id': 2, 'name': 'Vacancy 2'}]
        }
        # Правильный ответ дважды для 2 страниц, но установил 3 т.к. еще один вызов идет из _connect()
        mock_get.side_effect = [mock_response] * 3

        vacancies = self.hh_api.get_vacancies('Python', 2)

        self.assertEqual(mock_get.call_count, 3)

        expected_vacancies = [{'id': 1, 'name': 'Vacancy 1'}, {'id': 2, 'name': 'Vacancy 2'}] * 2
        self.assertEqual(len(vacancies), 4)
        self.assertEqual(vacancies, expected_vacancies)

    @patch('requests.get')
    def test_get_vacancies_no_items_key(self, mock_get):
        """Тестирование случая, когда в ответе нет ключа 'items'."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'other_data': 'some_value'}
        mock_get.return_value = mock_response

        vacancies = self.hh_api.get_vacancies('Test', 1)
        self.assertEqual(len(vacancies), 0)
        self.assertEqual(self.hh_api.vacancies, [])
