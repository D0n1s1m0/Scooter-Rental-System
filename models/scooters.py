"""Класс Scooter и функции работы с самокатами."""

from typing import List, Optional


class Scooter:
    """Электросамокат, доступный для аренды."""

    def __init__(
        self,
        scooter_id: int,
        model: str,
        charge: int,
        station_id: int,
        status: str = "available",
    ) -> None:
        """Создать объект самоката."""
        self.id = scooter_id
        self.model = model
        self.charge = charge
        self.station_id = station_id
        self.status = status

    def is_available(self) -> bool:
        """Проверить, доступен ли самокат для аренды."""
        return self.status == "available"

    def is_charged(self, min_charge: int = 20) -> bool:
        """Проверить, достаточен ли заряд для поездки."""
        return self.charge >= min_charge

    def set_status(self, status: str) -> None:
        """Изменить статус самоката."""
        self.status = status

    def __str__(self) -> str:
        """Строковое представление самоката."""
        return (f"{self.model} "
                f"(заряд {self.charge}%, "
                f"станция {self.station_id}, "
                f"статус {self.status})")


def add_scooter(
    scooters: List[Scooter],
    model: str,
    charge: int,
    station_id: int,
) -> Scooter:
    """Создать объект Scooter и добавить его в коллекцию."""
    new_id = max((s.id for s in scooters), default=0) + 1
    scooter = Scooter(new_id, model, charge, station_id)
    scooters.append(scooter)
    return scooter


def find_scooter_by_id(
    scooters: List[Scooter],
    scooter_id: int,
) -> Optional[Scooter]:
    """Найти самокат по идентификатору."""
    for s in scooters:
        if s.id == scooter_id:
            return s
    return None


def find_scooters(
    scooters: List[Scooter],
    query: str,
) -> List[Scooter]:
    """Найти самокаты по подстроке в модели."""
    q = query.lower()
    return [s for s in scooters if q in s.model.lower()]


def filter_scooters_by_charge(
    scooters: List[Scooter],
    min_charge: int,
) -> List[Scooter]:
    """Отобрать самокаты с зарядом не меньше min_charge."""
    return [s for s in scooters if s.is_charged(min_charge)]


def filter_available_scooters(
    scooters: List[Scooter],
) -> List[Scooter]:
    """Вернуть доступные самокаты."""
    return [s for s in scooters if s.is_available()]


def sort_scooters_by_charge(
    scooters: List[Scooter],
) -> List[Scooter]:
    """Отсортировать самокаты по заряду (убывание)."""
    return sorted(scooters, key=lambda s: s.charge, reverse=True)


def show_scooters(scooters: List[Scooter]) -> None:
    """Вывести список самокатов."""
    if not scooters:
        print("Список самокатов пуст.")
        return
    for s in scooters:
        print(f"  [{s.id}] {s}")
