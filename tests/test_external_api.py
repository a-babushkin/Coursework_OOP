from unittest import mock, TestCase
from unittest.mock import MagicMock
from src.external_api import HeadHunterAPI
from src.connect_api_exception import ConnectAPIError


class TestHeadHunterAPI(TestCase):

    @mock.patch('requests.Session')
    @mock.patch('os.getenv')
    def setUp(self, mock_getenv, mock_session):
        """Подготовка к тестам."""
        mock_getenv.return_value = 'http://mock.api.url'
        self.api = HeadHunterAPI()
        self.api._connect()

        self.mock_session = mock_session.return_value
        self.mock_session.get = MagicMock()

    def test_connection_success(self):
        """Тестируем успешное соединение с API."""
        self.mock_session.get.return_value.status_code = 200

        self.api._connect()
        self.mock_session.get.assert_called_once_with('http://mock.api.url')

    def test_connection_failure(self):
        """Тестируем неудачное соединение с API."""
        self.mock_session.get.return_value.status_code = 404

        with self.assertRaises(ConnectAPIError) as context:
            self.api._connect()

        self.assertEqual(str(context.exception), "Соединение не установлено. Код ошибки: 404")

    @mock.patch('requests.Session')
    @mock.patch('os.getenv')
    def test_get_vacancies_success(self, mock_getenv, mock_session):
        """Тестируем успешное получение вакансий."""
        mock_getenv.return_value = 'http://mock.api.url'

        response_mock = MagicMock()
        response_mock.status_code = 200
        response_mock.json.return_value = {'items': [{'id': 1, 'name': 'Developer'}]}

        self.mock_session.get.return_value = response_mock

        vacancies = self.api.get_vacancies('Developer', 1)

        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]['id'], 1)
        self.assertEqual(vacancies[0]['name'], 'Developer')

    @mock.patch('requests.Session')
    @mock.patch('os.getenv')
    def test_get_vacancies_connection_failure(self, mock_getenv, mock_session):
        """Тестируем ошибку при получении вакансий при неудачном соединении."""
        mock_getenv.return_value = 'http://mock.api.url'

        self.mock_session.get.side_effect = Exception("Connection Error")

        vacancies = self.api.get_vacancies('Developer', 1)

        self.assertEqual(vacancies, [{}])  # Проверяем, что в случае ошибки возвращается список с пустым словарем
