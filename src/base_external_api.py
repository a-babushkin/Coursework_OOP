from abc import ABC, abstractmethod


class JobWithAPI(ABC):
    """Абстрактный класс для работы с API."""

    @abstractmethod
    def _connect(self) -> None:
        """Устанавливает соединение с API."""
        pass

    @abstractmethod
    def get_vacancies(self, query: str, pages: int) -> list:
        """Получает вакансии по запросу."""
        pass
