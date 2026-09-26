"""Тесты класса Scooter и функций работы с самокатами."""

from models import Scooter
from models.scooters import (
    add_scooter,
    filter_available_scooters,
    filter_scooters_by_charge,
    find_scooter_by_id,
    find_scooters,
    sort_scooters_by_charge,
)


def test_scooter_creation():
    s = Scooter(1, "Xiaomi Mi 3", 95, 1)
    assert s.id == 1
    assert s.model == "Xiaomi Mi 3"
    assert s.charge == 95
    assert s.station_id == 1
    assert s.status == "available"


def test_is_available():
    s = Scooter(1, "A", 95, 1)
    assert s.is_available()
    s.set_status("in_use")
    assert not s.is_available()


def test_is_charged():
    s = Scooter(1, "A", 15, 1)
    assert not s.is_charged()
    assert s.is_charged(10)


def test_add_scooter():
    scooters = []
    s = add_scooter(scooters, "Xiaomi", 95, 1)
    assert s.id == 1
    assert len(scooters) == 1


def test_find_scooter_by_id():
    scooters = []
    add_scooter(scooters, "Xiaomi", 95, 1)
    assert find_scooter_by_id(scooters, 1) is not None
    assert find_scooter_by_id(scooters, 99) is None


def test_find_scooters():
    scooters = []
    add_scooter(scooters, "Xiaomi Mi 3", 95, 1)
    add_scooter(scooters, "Ninebot Max", 60, 2)
    assert len(find_scooters(scooters, "mi")) == 1


def test_filter_by_charge():
    scooters = []
    add_scooter(scooters, "A", 15, 1)
    add_scooter(scooters, "B", 80, 1)
    assert len(filter_scooters_by_charge(scooters, 50)) == 1


def test_filter_available():
    scooters = []
    s1 = add_scooter(scooters, "A", 95, 1)
    add_scooter(scooters, "B", 80, 1)
    s1.set_status("in_use")
    assert len(filter_available_scooters(scooters)) == 1


def test_sort_by_charge():
    scooters = []
    add_scooter(scooters, "A", 30, 1)
    add_scooter(scooters, "B", 80, 1)
    ordered = sort_scooters_by_charge(scooters)
    assert ordered[0].charge == 80