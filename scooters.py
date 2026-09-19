"""Функции для работы с самокатами."""


def add_scooter(
    scooters: dict[int, dict],
    model: str,
    charge: int,
    station: str,
) -> int:
    """Добавить самокат в словарь scooters.

    Возвращает идентификатор добавленного самоката.
    """
    scooter_id = max(scooters.keys(), default=0) + 1
    scooters[scooter_id] = {
        "model": model,
        "charge": charge,
        "station": station,
        "status": "available",
    }
    return scooter_id


def find_scooter(scooters: dict[int, dict], query: str) -> list[int]:
    """Найти самокаты по подстроке в модели.

    Возвращает список идентификаторов подходящих самокатов.
    """
    query_lower = query.lower()
    return [
        sid for sid, s in scooters.items()
        if query_lower in s["model"].lower()
    ]


def filter_scooters_by_charge(
    scooters: dict[int, dict],
    min_charge: int,
) -> list[int]:
    """Отобрать самокаты с зарядом не меньше min_charge."""
    return [
        sid for sid, s in scooters.items()
        if s["charge"] >= min_charge
    ]


def sort_scooters_by_charge(
    scooters: dict[int, dict],
) -> list[tuple[int, dict]]:
    """Отсортировать самокаты по заряду (убывание)."""
    return sorted(
        scooters.items(),
        key=lambda item: item[1]["charge"],
        reverse=True,
    )


def get_scooter_status(
    scooters: dict[int, dict],
    scooter_id: int,
) -> str:
    """Вернуть текстовый статус самоката."""
    scooter = scooters.get(scooter_id)
    if scooter is None:
        return "Самокат не найден"
    statuses = {
        "available": "Доступен",
        "in_use": "В аренде",
        "maintenance": "На обслуживании",
    }
    return statuses.get(scooter["status"], "Неизвестный статус")


def get_available_scooters(scooters: dict[int, dict]) -> list[int]:
    """Вернуть идентификаторы доступных самокатов."""
    return [
        sid for sid, s in scooters.items()
        if s["status"] == "available"
    ]
