"""Класс Station и функции работы со станциями."""

from typing import List, Optional


class Station:
    """Станция парковки самокатов."""

    def __init__(
        self,
        station_id: int,
        name: str,
        address: str,
        capacity: int,
    ) -> None:
        """Создать объект станции."""
        self.id = station_id
        self.name = name
        self.address = address
        self.capacity = capacity

    def __str__(self) -> str:
        """Строковое представление станции."""
        return f"{self.name} ({self.address}), мест: {self.capacity}"

    @classmethod
    def from_data(cls, data: dict) -> "Station":
        """Создать станцию из данных JSON."""
        return cls(
            station_id=data["id"],
            name=data["name"],
            address=data["address"],
            capacity=data["capacity"],
        )

    def to_data(self) -> dict:
        """Преобразовать объект в данные для JSON."""
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "capacity": self.capacity,
        }


def add_station(
    stations: List[Station],
    name: str,
    address: str,
    capacity: int,
) -> Station:
    """Создать объект Station и добавить его в коллекцию."""
    new_id = max((s.id for s in stations), default=0) + 1
    station = Station(new_id, name, address, capacity)
    stations.append(station)
    return station


def find_station_by_id(
    stations: List[Station],
    station_id: int,
) -> Optional[Station]:
    """Найти станцию по идентификатору."""
    for s in stations:
        if s.id == station_id:
            return s
    return None


def show_stations(stations: List[Station]) -> None:
    """Вывести список станций."""
    if not stations:
        print("Станций нет.")
        return
    for s in stations:
        print(f"  [{s.id}] {s}")
