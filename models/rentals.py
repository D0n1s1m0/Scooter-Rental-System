"""Класс Rental и функции работы с арендами."""

from typing import List, Optional

from .scooters import Scooter
from .users import User

TARIFF_PER_MINUTE = 5.0
UNLOCK_FEE = 30.0
DISCOUNT_THRESHOLD = 60
DISCOUNT_RATE = 0.10


class Rental:
    """Аренда самоката пользователем."""

    def __init__(
        self,
        rental_id: int,
        scooter: Scooter,
        user: User,
        rental_date: str,
        minutes: float,
        total: float,
        is_finished: bool = False,
    ) -> None:
        """Создать объект аренды."""
        self.id = rental_id
        self.scooter = scooter
        self.user = user
        self.rental_date = rental_date
        self.minutes = minutes
        self.total = total
        self.is_finished = is_finished

    def finish(self) -> None:
        """Завершить аренду и освободить самокат."""
        self.is_finished = True
        self.scooter.set_status("available")

    def __str__(self) -> str:
        """Строковое представление аренды."""
        state = "завершена" if self.is_finished else "активна"
        return (f"Аренда #{self.id}: {self.scooter.model} "
                f"для {self.user.name}, "
                f"{self.rental_date}, {self.minutes:.0f} мин, "
                f"{self.total:.2f} руб. [{state}]")


def calculate_base_cost(minutes: float) -> float:
    """Базовая стоимость поездки."""
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
    rentals: List[Rental],
    scooter: Scooter,
    rental_date: str,
) -> bool:
    """Проверить, свободен ли самокат на указанную дату."""
    for r in rentals:
        if r.is_finished:
            continue
        if r.scooter.id == scooter.id and r.rental_date == rental_date:
            return False
    return True


def create_rental(
    rentals: List[Rental],
    scooter: Scooter,
    user: User,
    rental_date: str,
    minutes: float,
) -> Optional[Rental]:
    """Создать аренду, если самокат свободен."""
    if not is_scooter_available(rentals, scooter, rental_date):
        return None
    base = calculate_base_cost(minutes)
    discount = calculate_discount(base, minutes)
    total = calculate_total(base, discount)
    new_id = max((r.id for r in rentals), default=0) + 1
    rental = Rental(new_id, scooter, user, rental_date, minutes, total)
    scooters_status = "in_use"
    scooter.set_status(scooters_status)
    rentals.append(rental)
    return rental


def cancel_rental(
    rentals: List[Rental],
    rental_id: int,
) -> bool:
    """Отменить (завершить) аренду по идентификатору."""
    for r in rentals:
        if r.id == rental_id and not r.is_finished:
            r.finish()
            return True
    return False


def get_total_revenue(rentals: List[Rental]) -> float:
    """Общая выручка по всем арендам."""
    return round(sum(r.total for r in rentals), 2)


def show_rentals(rentals: List[Rental]) -> None:
    """Вывести список аренд."""
    if not rentals:
        print("Аренд пока нет.")
        return
    for r in rentals:
        print(f"  {r}")