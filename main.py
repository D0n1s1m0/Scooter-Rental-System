# main.py
"""
Система аренды самокатов — ПР1.
Начальный сценарий: расчёт стоимости аренды самоката.
"""

import math

# ---------- Константы тарифов ----------
TARIFF_PER_MINUTE = 5.0        # руб. за минуту
UNLOCK_FEE = 30.0              # руб. за разблокировку
DISCOUNT_THRESHOLD = 60        # минут, после которых действует скидка
DISCOUNT_RATE = 0.10           # 10% скидка

# ---------- Ввод данных пользователем ----------
print("=== Система аренды самокатов ===")
print("Расчёт стоимости поездки\n")

user_name = input("Введите ваше имя: ").strip()

try:
    minutes = float(input("Введите длительность поездки (в минутах): "))
except ValueError:
    print("Ошибка: введите числовое значение.")
    minutes = 0.0

# ---------- Расчёт стоимости ----------
if minutes <= 0:
    print(f"\n{user_name}, поездка не была совершена. Стоимость: 0 руб.")
else:
    base_cost = UNLOCK_FEE + minutes * TARIFF_PER_MINUTE

    if minutes > DISCOUNT_THRESHOLD:
        discount = base_cost * DISCOUNT_RATE
        total_cost = base_cost - discount
        print(f"\nПрименена скидка {int(DISCOUNT_RATE * 100)}% "
              f"(поездка дольше {DISCOUNT_THRESHOLD} минут)")
    else:
        discount = 0.0
        total_cost = base_cost

    # Округление до 2 знаков
    total_cost = round(total_cost, 2)

    # ---------- Вывод результата ----------
    print(f"\n{user_name}, ваш чек:")
    print(f"  Разблокировка:      {UNLOCK_FEE:.2f} руб.")
    print(f"  Поездка ({minutes:.0f} мин): {minutes * TARIFF_PER_MINUTE:.2f} руб.")
    if discount > 0:
        print(f"  Скидка:            -{discount:.2f} руб.")
    print(f"  ------------------------------")
    print(f"  Итого:              {total_cost:.2f} руб.")

    # Проверка на целое число минут (демонстрация math)
    if math.floor(minutes) == minutes:
        print(f"\nВремя поездки: ровно {int(minutes)} мин.")