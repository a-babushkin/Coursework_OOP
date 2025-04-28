from typing import Any


class ConnectAPIError(Exception):
    """Класс исключения для ошибок соединения"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.message = args[0] if args else "Неизвестная ошибка."

    def __str__(self) -> str:
        return self.message
