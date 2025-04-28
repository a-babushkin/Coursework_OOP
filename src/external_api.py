import os
import requests
from dotenv import load_dotenv

from src.base_external_api import JobWithAPI
from src.connect_api_exception import ConnectAPIError


class HeadHunterAPI(JobWithAPI):
    """Класс для работы с Head Hunter API."""

    def __init__(self):
        load_dotenv()
        self.__url = os.getenv("BASE_URL")
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 10}  # , 'only_with_salary': True
        self.vacancies = []
        self.__session = None

    def _connect(self) -> None:
        """Устанавливаем соединение (например, создаем сессию и проверяем соединение с сервером)."""
        self.__session = requests.Session()
        response = self.__session.get(os.getenv("BASE_URL"))
        if response.status_code != 200:
            raise ConnectAPIError(f"Соединение не установлено. Код ошибки: {response.status_code}")
        print("Соединение с API установлено.")

    def get_vacancies(self, query: str, pages: int) -> list:
        """Получаем вакансии по запросу из API и возвращаем сырой список вакансий."""
        try:
            self._connect()
        except ConnectAPIError as connect_error:
            print(connect_error)
            return [{}]
        else:
            self.__params['text'] = query
            while self.__params.get('page') != pages:
                response = self.__session.get(os.getenv("BASE_URL"), headers=self.__headers, params=self.__params)

                if response.status_code != 200:
                    print(response)
                    raise ConnectAPIError(f"Ошибка при получении данных: {response.status_code} {response.text}")
                loaded_vacancies = response.json().get('items', [])
                self.vacancies.extend(loaded_vacancies)
                self.__params['page'] += 1
            return self.vacancies
