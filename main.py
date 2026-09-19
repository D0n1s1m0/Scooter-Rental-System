"""Система аренды самокатов — ПР2.

Точка запуска программы. Меню и взаимодействие с пользователем.
"""

from scooters import (
    add_scooter,
    filter_scooters_by_charge,
    find_scooter,
    get_available_scooters,
    get_scooter_status,
    sort_scooters_by_charge,
)
from rentals import (
    calculate_base_cost,
    calculate_discount,
    calculate_total,
    cancel_rental,
    create_rental,
    get_total_revenue,
    is_scooter_available,
)
from storage import (
    load_rentals,
    load_scooters,
    save_rentals,
    save_scooters,
)
from utils import input_date, input_float, input_int


def get_user_name() -> str:
    """Небольшой опрос, чтобы обращаться к человеку по имени."""
    return input("Введите ваше имя: ").strip()


def show_scooters(scooters: dict[int, dict]) -> None:
    """Вывести список самокатов."""
    if not scooters:
        print("Список самокатов пуст.")
        return
    print()
    print(f"{'ID':<4}{'Модель':<20}{'Заряд':<8}"
          f"{'Станция':<20}{'Статус'}")
    print("-" * 70)
    for sid, s in scooters.items():
        status = get_scooter_status(scooters, sid)
        print(
            f"{sid:<4}"
            f"{s['model']:<20}"
            f"{s['charge']:<8}"
            f"{s['station']:<20}"
            f"{status}"
        )


def show_rentals(rentals: list[dict]) -> None:
    """Вывести список аренд."""
    if not rentals:
        print("Аренд пока нет.")
        return
    print()
    print(f"{'Самокат':<10}{'Дата':<14}{'Минут':<8}{'Итого':<10}")
    print("-" * 45)
    for r in rentals:
        print(
            f"{r['scooter_id']:<10}"
            f"{r['date']:<14}"
            f"{r['minutes']:<8}"
            f"{r['total']:<10}"
        )


def show_receipt(
    user_name: str,
    minutes: float,
    base_cost: float,
    discount: float,
    total_cost: float,
) -> None:
    """Печать чека (функция из ПР1, адаптированная под новые данные)."""
    print()
    print(f"{user_name}, ваш чек:")
    print(f"  Базовая стоимость:  {base_cost:.2f} руб.")
    if discount > 0:
        print(f"  Скидка:            -{discount:.2f} руб.")
    print("  ------------------------------")
    print(f"  Итого:              {total_cost:.2f} руб.")


def menu() -> None:
    """Главное меню приложения."""
    print()
    print("=== Система аренды самокатов ===")
    print("1. Показать самокаты")
    print("2. Найти самокат по модели")
    print("3. Показать доступные самокаты")
    print("4. Отсортировать по заряду")
    print("5. Фильтр по минимальному заряду")
    print("6. Начать аренду")
    print("7. Отменить аренду")
    print("8. Показать аренды")
    print("9. Статистика (выручка)")
    print("0. Выход")


def handle_find(scooters: dict[int, dict]) -> None:
    """Обработать поиск самоката по модели."""
    query = input("Введите часть модели: ")
    found = find_scooter(scooters, query)
    if found:
        for sid in found:
            model = scooters[sid]["model"]
            print(f"  Найден: {sid} — {model}")
    else:
        print("Ничего не найдено.")


def handle_available(scooters: dict[int, dict]) -> None:
    """Обработать вывод доступных самокатов."""
    available = get_available_scooters(scooters)
    if available:
        for sid in available:
            print(f"  {sid}: {scooters[sid]['model']}")
    else:
        print("Нет доступных самокатов.")


def handle_sort(scooters: dict[int, dict]) -> None:
    """Обработать сортировку самокатов по заряду."""
    for sid, s in sort_scooters_by_charge(scooters):
        print(f"  {sid}: {s['model']} — заряд {s['charge']}%")


def handle_filter(scooters: dict[int, dict]) -> None:
    """Обработать фильтр по минимальному заряду."""
    min_charge = input_int("Минимальный заряд: ")
    found = filter_scooters_by_charge(scooters, min_charge)
    if found:
        for sid in found:
            print(f"  {sid}: {scooters[sid]['model']} — "
                  f"{scooters[sid]['charge']}%")
    else:
        print("Нет самокатов с таким зарядом.")


def handle_start_rental(
    scooters: dict[int, dict],
    rentals: list[dict],
    user_name: str,
) -> None:
    """Обработать начало аренды."""
    scooter_id = input_int("ID самоката: ")
    if scooter_id not in scooters:
        print("Самокат не найден.")
        return
    rental_date = input_date("Дата аренды (ДД.ММ.ГГГГ): ")
    if not is_scooter_available(rentals, scooter_id, rental_date):
        print("Самокат уже занят на эту дату.")
        return
    minutes = input_float("Длительность поездки (мин): ")
    base = calculate_base_cost(minutes)
    discount = calculate_discount(base, minutes)
    total = calculate_total(base, discount)
    create_rental(rentals, scooter_id, rental_date, minutes)
    show_receipt(user_name, minutes, base, discount, total)


def handle_cancel_rental(rentals: list[dict]) -> None:
    """Обработать отмену аренды."""
    scooter_id = input_int("ID самоката для отмены: ")
    if cancel_rental(rentals, scooter_id):
        print("Аренда отменена.")
    else:
        print("Аренда не найдена.")


def handle_statistics(rentals: list[dict]) -> None:
    """Обработать вывод статистики."""
    revenue = get_total_revenue(rentals)
    print(f"Общая выручка: {revenue:.2f} руб.")


def main() -> None:
    """Точка входа: меню и вызов функций проекта."""
    user_name = get_user_name()
    print(f"\nЗдравствуйте, {user_name}!")

    scooters = load_scooters()
    rentals = load_rentals()

    if not scooters:
        add_scooter(scooters, "Xiaomi Mi 3", 95, "Станция A")
        add_scooter(scooters, "Ninebot Max", 60, "Станция B")
        add_scooter(scooters, "Kugoo S3", 20, "Станция A")

    while True:
        menu()
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_scooters(scooters)
        elif choice == "2":
            handle_find(scooters)
        elif choice == "3":
            handle_available(scooters)
        elif choice == "4":
            handle_sort(scooters)
        elif choice == "5":
            handle_filter(scooters)
        elif choice == "6":
            handle_start_rental(scooters, rentals, user_name)
        elif choice == "7":
            handle_cancel_rental(rentals)
        elif choice == "8":
            show_rentals(rentals)
        elif choice == "9":
            handle_statistics(rentals)
        elif choice == "0":
            save_scooters(scooters)
            save_rentals(rentals)
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()
