"""Тесты функций работы с самокатами."""

from scooters import (
    add_scooter,
    filter_scooters_by_charge,
    find_scooter,
    get_available_scooters,
    sort_scooters_by_charge,
)


def test_add_scooter():
    scooters = {}
    sid = add_scooter(scooters, "Xiaomi Mi 3", 95, "A")
    assert sid == 1
    assert len(scooters) == 1
    assert scooters[1]["model"] == "Xiaomi Mi 3"


def test_find_scooter():
    scooters = {}
    add_scooter(scooters, "Xiaomi Mi 3", 95, "A")
    add_scooter(scooters, "Ninebot Max", 60, "B")
    assert find_scooter(scooters, "mi") == [1]


def test_filter_by_charge():
    scooters = {}
    add_scooter(scooters, "A", 30, "A")
    add_scooter(scooters, "B", 80, "B")
    assert filter_scooters_by_charge(scooters, 50) == [2]


def test_sort_by_charge():
    scooters = {}
    add_scooter(scooters, "A", 30, "A")
    add_scooter(scooters, "B", 80, "B")
    ordered = sort_scooters_by_charge(scooters)
    assert ordered[0][0] == 2


def test_available_scooters():
    scooters = {}
    add_scooter(scooters, "A", 95, "A")
    scooters[1]["status"] = "in_use"
    assert get_available_scooters(scooters) == []
