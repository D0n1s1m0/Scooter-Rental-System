"""Функции для работы с арендами."""

from datetime import date

TARIFF_PER_MINUTE = 5.0
UNLOCK_FEE = 30.0
DISCOUNT_THRESHOLD = 60
DISCOUNT_RATE = 0.10


def calculate_base_cost(minutes: float) -> float:
    """Автоматический расчёт базовой стоимости поездки."""
    return UNLOCK_FEE + minutes * TARIFF_PER_MINUTE


def calculate_discount(base_cost: float, minutes: float) -> float:
    """Скидка 10% при поездке дольше 60 минут."""
    if minutes > DISCOUNT_THRESHOLD:
        return base_cost * DISCOUNT_RATE
    return 0.0


def calculate_total(base_cost: float, discount: float) -> float:
    """Итоговая стоимость с округлением до 2 знаков."""
    return round(base_cost - discount, 2)


def is_scooter_available(
    rentals: list[dict],
    scooter_id: int,
    rental_date: date,
) -> bool:
    """Проверить, свободен ли самокат на указанную дату."""
    for r in rentals:
        if (r["scooter_id"] == scooter_id
                and r["date"] == rental_date.isoformat()):
            return False
    return True


def create_rental(
    rentals: list[dict],
    scooter_id: int,
    rental_date: date,
    minutes: float,
) -> dict:
    """Создать новую аренду с расчётом стоимости."""
    base_cost = calculate_base_cost(minutes)
    discount = calculate_discount(base_cost, minutes)
    total = calculate_total(base_cost, discount)
    rental = {
        "scooter_id": scooter_id,
        "date": rental_date.isoformat(),
        "minutes": minutes,
        "total": total,
    }
    rentals.append(rental)
    return rental


def cancel_rental(rentals: list[dict], scooter_id: int) -> bool:
    """Отменить аренду по идентификатору самоката."""
    for i, r in enumerate(rentals):
        if r["scooter_id"] == scooter_id:
            rentals.pop(i)
            return True
    return False


def get_total_revenue(rentals: list[dict]) -> float:
    """Сумма всех платежей (статистика)."""
    return round(sum(r["total"] for r in rentals), 2)
