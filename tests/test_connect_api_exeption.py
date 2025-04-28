import unittest
from src.connect_api_exception import ConnectAPIError


class TestConnectAPIError(unittest.TestCase):

    def test_default_message(self):
        """Тестирование использования сообщения по умолчанию."""
        error = ConnectAPIError()
        self.assertEqual(str(error), 'Неизвестная ошибка.')

    def test_custom_message(self):
        """Тестирование передачи пользовательского сообщения."""
        error = ConnectAPIError("Ошибка соединения с API")
        self.assertEqual(str(error), 'Ошибка соединения с API')

    def test_multiple_arguments(self):
        """Тестирование передачи нескольких аргументов."""
        error = ConnectAPIError("Ошибка", "Дополнительная информация")
        self.assertEqual(str(error), 'Ошибка')
