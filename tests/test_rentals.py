from models import Scooter, User
from models.rentals import (
    calculate_base_cost,
    calculate_discount,
    calculate_total,
    create_rental,
    is_scooter_available,
)


def _make_objects():
    """Вспомогательная функция: свежие объекты для теста."""
    scooter = Scooter(1, "Xiaomi", 95, 1)
    user = User(1, "Иван", "i@e.com")
    return scooter, user


def test_base_cost():
    assert calculate_base_cost(10) == 80.0


def test_discount_applied():
    base = calculate_base_cost(100)
    assert round(calculate_discount(base, 100), 2) == 53.0


def test_discount_not_applied():
    base = calculate_base_cost(30)
    assert calculate_discount(base, 30) == 0.0


def test_total_cost():
    assert calculate_total(530.0, 53.0) == 477.0


def test_is_scooter_available():
    scooter, _ = _make_objects()
    assert is_scooter_available([], scooter, "2026-09-15")


def test_create_rental_links_objects():
    scooter, user = _make_objects()
    rentals = []
    rental = create_rental(rentals, scooter, user, "2026-09-15", 30)
    assert rental is not None
    assert rental.scooter is scooter
    assert rental.user is user


def test_duplicate_rental_forbidden():
    scooter, user = _make_objects()
    rentals = []
    create_rental(rentals, scooter, user, "2026-09-15", 30)
    assert not is_scooter_available(rentals, scooter, "2026-09-15")


def test_finish_rental_frees_scooter():
    scooter, user = _make_objects()
    rentals = []
    rental = create_rental(rentals, scooter, user, "2026-09-15", 30)
    rental.finish()
    assert is_scooter_available(rentals, scooter, "2026-09-15")