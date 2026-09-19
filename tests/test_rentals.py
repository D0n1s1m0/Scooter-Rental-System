"""Тесты функций аренды."""

from datetime import date

from rentals import (
    calculate_base_cost,
    calculate_discount,
    calculate_total,
    create_rental,
    is_scooter_available,
)


def test_base_cost():
    assert calculate_base_cost(10) == 80.0


def test_discount_applied():
    base = calculate_base_cost(100)
    discount = calculate_discount(base, 100)
    assert round(discount, 2) == 53.0


def test_discount_not_applied():
    base = calculate_base_cost(30)
    assert calculate_discount(base, 30) == 0.0


def test_total_cost():
    base = 530.0
    discount = 53.0
    assert calculate_total(base, discount) == 477.0


def test_is_scooter_available():
    rentals = []
    assert is_scooter_available(rentals, 1, date(2026, 9, 15))


def test_duplicate_rental_forbidden():
    rentals = []
    create_rental(rentals, 1, date(2026, 9, 15), 30)
    assert not is_scooter_available(rentals, 1, date(2026, 9, 15))
