"""Сохранение и загрузка данных проекта в JSON-файлах."""

import json
import os

DATA_DIR = "data"
SCOOTERS_FILE = os.path.join(DATA_DIR, "scooters.json")
RENTALS_FILE = os.path.join(DATA_DIR, "rentals.json")


def _ensure_data_dir() -> None:
    """Создать каталог data, если его нет."""
    os.makedirs(DATA_DIR, exist_ok=True)


def load_scooters(filename: str = SCOOTERS_FILE) -> dict[int, dict]:
    """Загрузить самокаты из JSON-файла."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            raw = json.load(f)
        return {int(k): v for k, v in raw.items()}
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print(f"Ошибка: файл {filename} повреждён. Создаём пустой список.")
        return {}


def save_scooters(scooters: dict[int, dict], filename: str = SCOOTERS_FILE) -> None:
    """Сохранить самокаты в JSON-файл."""
    _ensure_data_dir()
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(scooters, f, ensure_ascii=False, indent=2)


def load_rentals(filename: str = RENTALS_FILE) -> list[dict]:
    """Загрузить аренды из JSON-файла."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: файл {filename} повреждён. Создаём пустой список.")
        return []


def save_rentals(rentals: list[dict], filename: str = RENTALS_FILE) -> None:
    """Сохранить аренды в JSON-файл."""
    _ensure_data_dir()
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(rentals, f, ensure_ascii=False, indent=2)
