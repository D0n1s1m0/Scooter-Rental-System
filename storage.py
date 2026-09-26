"""Сохранение и загрузка данных проекта в JSON-файлах."""

import json
import os
from typing import List

from models import Rental, Scooter, Station, User
from models.rentals import (
    calculate_base_cost,
    calculate_discount,
    calculate_total,
)

DATA_DIR = "data"
SCOOTERS_FILE = os.path.join(DATA_DIR, "scooters.json")
USERS_FILE = os.path.join(DATA_DIR, "users.json")
STATIONS_FILE = os.path.join(DATA_DIR, "stations.json")
RENTALS_FILE = os.path.join(DATA_DIR, "rentals.json")


def _ensure_data_dir() -> None:
    """Создать каталог data, если его нет."""
    os.makedirs(DATA_DIR, exist_ok=True)


def _load_json(filename: str):
    """Прочитать JSON-файл, вернуть данные или None."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print(f"Ошибка: файл {filename} повреждён.")
        return None


def _save_json(filename: str, data) -> None:
    """Записать данные в JSON-файл."""
    _ensure_data_dir()
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_scooters(filename: str = SCOOTERS_FILE) -> List[Scooter]:
    """Загрузить самокаты из JSON в объекты Scooter."""
    raw = _load_json(filename)
    if raw is None:
        return []
    return [
        Scooter(
            scooter_id=item["id"],
            model=item["model"],
            charge=item["charge"],
            station_id=item["station_id"],
            status=item.get("status", "available"),
        )
        for item in raw
    ]


def save_scooters(
    scooters: List[Scooter],
    filename: str = SCOOTERS_FILE,
) -> None:
    """Сохранить объекты Scooter в JSON."""
    data = [
        {
            "id": s.id,
            "model": s.model,
            "charge": s.charge,
            "station_id": s.station_id,
            "status": s.status,
        }
        for s in scooters
    ]
    _save_json(filename, data)


def load_users(filename: str = USERS_FILE) -> List[User]:
    """Загрузить пользователей из JSON в объекты User."""
    raw = _load_json(filename)
    if raw is None:
        return []
    return [User.from_data(item) for item in raw]


def save_users(
    users: List[User],
    filename: str = USERS_FILE,
) -> None:
    """Сохранить объекты User в JSON."""
    _save_json(filename, [u.to_data() for u in users])


def load_stations(filename: str = STATIONS_FILE) -> List[Station]:
    """Загрузить станции из JSON в объекты Station."""
    raw = _load_json(filename)
    if raw is None:
        return []
    return [Station.from_data(item) for item in raw]


def save_stations(
    stations: List[Station],
    filename: str = STATIONS_FILE,
) -> None:
    """Сохранить объекты Station в JSON."""
    _save_json(filename, [s.to_data() for s in stations])


def load_rentals(
    scooters: List[Scooter],
    users: List[User],
    filename: str = RENTALS_FILE,
) -> List[Rental]:
    """Загрузить аренды, восстановив связи с объектами."""
    raw = _load_json(filename)
    if raw is None:
        return []
    rentals: List[Rental] = []
    for item in raw:
        scooter = next(
            (s for s in scooters if s.id == item["scooter_id"]),
            None,
        )
        user = next(
            (u for u in users if u.id == item["user_id"]),
            None,
        )
        if scooter is None or user is None:
            continue
        rental = Rental(
            rental_id=item["id"],
            scooter=scooter,
            user=user,
            rental_date=item["rental_date"],
            minutes=item["minutes"],
            total=item["total"],
            is_finished=item.get("is_finished", False),
        )
        rentals.append(rental)
    return rentals


def save_rentals(
    rentals: List[Rental],
    filename: str = RENTALS_FILE,
) -> None:
    """Сохранить объекты Rental в JSON."""
    data = [
        {
            "id": r.id,
            "scooter_id": r.scooter.id,
            "user_id": r.user.id,
            "rental_date": r.rental_date,
            "minutes": r.minutes,
            "total": r.total,
            "is_finished": r.is_finished,
        }
        for r in rentals
    ]
    _save_json(filename, data)