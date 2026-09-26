"""Тесты класса Station."""

from models import Station
from models.stations import add_station, find_station_by_id


def test_station_creation():
    st = Station(1, "Станция A", "ул. Ленина, 1", 20)
    assert st.id == 1
    assert st.name == "Станция A"
    assert st.capacity == 20


def test_add_station():
    stations = []
    st = add_station(stations, "A", "addr", 10)
    assert st.id == 1
    assert len(stations) == 1


def test_find_station_by_id():
    stations = []
    add_station(stations, "A", "addr", 10)
    assert find_station_by_id(stations, 1) is not None
    assert find_station_by_id(stations, 99) is None