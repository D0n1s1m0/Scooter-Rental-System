"""Вспомогательные функции ввода."""

from datetime import datetime


def input_int(prompt: str) -> int:
    """Запросить целое число, повторяя при ошибке."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")


def input_float(prompt: str) -> float:
    """Запросить число, повторяя при ошибке."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число.")


def input_date(prompt: str) -> str:
    """Запросить дату в формате ДД.ММ.ГГГГ, вернуть ISO-строку."""
    while True:
        try:
            d = datetime.strptime(input(prompt), "%d.%m.%Y").date()
            return d.isoformat()
        except ValueError:
            print("Ошибка: неверный формат. Пример: 15.09.2026")