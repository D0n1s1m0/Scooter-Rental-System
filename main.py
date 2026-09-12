# main.py
"""
Система аренды самокатов — ПР1.
Сценарий: расчёт стоимости поездки на самокате.
"""

import math

# ---------- Константы тарифов ----------
TARIFF_PER_MINUTE = 5.0     # руб. за минуту
UNLOCK_FEE = 30.0           # руб. за разблокировку
DISCOUNT_THRESHOLD = 60     # минут, после которых действует скидка
DISCOUNT_RATE = 0.10        # 10% скидка


# ---------- Функции ----------
def get_user_name():
    """Запрашивает имя пользователя."""
    name = input("Введите ваше имя: ").strip()
    return name


def get_trip_minutes():
    """Запрашивает длительность поездки и преобразует к float."""
    raw = input("Введите длительность поездки (в минутах): ")
    try:
        minutes = float(raw)
    except ValueError:
        print("Ошибка: введите числовое значение.")
        minutes = 0.0
    return minutes


def calculate_base_cost(minutes):
    """Возвращает базовую стоимость поездки без скидки."""
    return UNLOCK_FEE + minutes * TARIFF_PER_MINUTE


def calculate_discount(base_cost, minutes):
    """Возвращает размер скидки: 10% при поездке дольше 60 минут."""
    if minutes > DISCOUNT_THRESHOLD:
        return base_cost * DISCOUNT_RATE /100
    return 0.0


def calculate_total(base_cost, discount):
    """Возвращает итоговую стоимость с округлением до 2 знаков."""
    return round(base_cost - discount, 2)


def print_receipt(user_name, minutes, base_cost, discount, total_cost):
    """Печатает чек пользователю."""
    print(f"\n{user_name}, ваш чек:")
    print(f"  Разблокировка:        {UNLOCK_FEE:.2f} руб.")
    print(f"  Поездка ({minutes:.0f} мин):   {minutes * TARIFF_PER_MINUTE:.2f} руб.")
    if discount > 0:
        print(f"  Скидка:              -{discount:.2f} руб.")
    print(f"  --------------------------------")
    print(f"  Итого:                {total_cost:.2f} руб.")


def is_whole_minutes(minutes):
    """Проверяет, является ли длительность целым числом минут."""
    return math.floor(minutes) == minutes


# ---------- Основной сценарий ----------
def main():
    print("=== Система аренды самокатов ===")
    print("Расчёт стоимости поездки\n")

    user_name = get_user_name()
    minutes = get_trip_minutes()

    if minutes <= 0:
        print(f"\n{user_name}, поездка не была совершена. Стоимость: 0 руб.")
        return

    base_cost = calculate_base_cost(minutes)
    discount = calculate_discount(base_cost, minutes)

    if discount > 0:
        print(f"\nПрименена скидка {int(DISCOUNT_RATE * 100)}% "
              f"(поездка дольше {DISCOUNT_THRESHOLD} минут)")

    total_cost = calculate_total(base_cost, discount)
    print_receipt(user_name, minutes, base_cost, discount, total_cost)

    if is_whole_minutes(minutes):
        print(f"\nВремя поездки: ровно {int(minutes)} мин.")


# ---------- Точка входа ----------
if __name__ == "__main__":
    main()