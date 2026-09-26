"""Система аренды самокатов — ПР3.

Объектная модель: Scooter, User, Station, Rental.
"""

from typing import List

from models import Rental, Scooter, Station, User
from models.rentals import (
    cancel_rental,
    create_rental,
    get_total_revenue,
    show_rentals,
)
from models.scooters import (
    add_scooter,
    filter_available_scooters,
    find_scooter_by_id,
    find_scooters,
    show_scooters,
    sort_scooters_by_charge,
)
from models.stations import add_station, show_stations
from models.users import add_user, find_user_by_id, show_users
from storage import (
    load_rentals,
    load_scooters,
    load_stations,
    load_users,
    save_rentals,
    save_scooters,
    save_stations,
    save_users,
)
from utils import input_date, input_float, input_int


def get_user_name() -> str:
    """Небольшой опрос."""
    return input("Введите ваше имя: ").strip()


def menu() -> None:
    """Главное меню."""
    print("\n=== Система аренды самокатов ===")
    print("1. Показать самокаты")
    print("2. Найти самокат по модели")
    print("3. Показать доступные самокаты")
    print("4. Отсортировать самокаты по заряду")
    print("5. Показать пользователей")
    print("6. Показать станции")
    print("7. Начать аренду")
    print("8. Завершить аренду")
    print("9. Показать аренды")
    print("10. Статистика (выручка)")
    print("0. Выход")


def create_new_rental(
    rentals: List[Rental],
    scooters: List[Scooter],
    users: List[User],
) -> None:
    """Сценарий создания аренды через объекты."""
    scooter_id = input_int("ID самоката: ")
    scooter = find_scooter_by_id(scooters, scooter_id)
    if scooter is None:
        print("Самокат не найден.")
        return

    user_id = input_int("ID пользователя: ")
    user = find_user_by_id(users, user_id)
    if user is None:
        print("Пользователь не найден.")
        return

    rental_date = input_date("Дата аренды (ДД.ММ.ГГГГ): ")
    minutes = input_float("Длительность поездки (мин): ")

    rental = create_rental(
        rentals, scooter, user, rental_date, minutes,
    )
    if rental is None:
        print("Самокат уже занят на эту дату.")
        return

    print(f"\nАренда #{rental.id} создана.")
    print(rental)


def main() -> None:
    """Точка входа."""
    user_name = get_user_name()
    print(f"\nЗдравствуйте, {user_name}!")

    scooters = load_scooters()
    users = load_users()
    stations = load_stations()
    rentals = load_rentals(scooters, users)

    if not scooters:
        add_station(stations, "Станция A", "ул. Ленина, 1", 20)
        add_station(stations, "Станция B", "ул. Мира, 15", 15)
        add_user(users, "Иван Петров", "ivan@example.com")
        add_user(users, "Анна Смирнова", "anna@example.com")
        add_scooter(scooters, "Xiaomi Mi 3", 95, 1)
        add_scooter(scooters, "Ninebot Max", 60, 2)
        add_scooter(scooters, "Kugoo S3", 20, 1)

    while True:
        menu()
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_scooters(scooters)
        elif choice == "2":
            q = input("Часть модели: ")
            show_scooters(find_scooters(scooters, q))
        elif choice == "3":
            show_scooters(filter_available_scooters(scooters))
        elif choice == "4":
            show_scooters(sort_scooters_by_charge(scooters))
        elif choice == "5":
            show_users(users)
        elif choice == "6":
            show_stations(stations)
        elif choice == "7":
            create_new_rental(rentals, scooters, users)
        elif choice == "8":
            rid = input_int("ID аренды для завершения: ")
            print("Аренда завершена." if cancel_rental(rentals, rid)
                  else "Аренда не найдена.")
        elif choice == "9":
            show_rentals(rentals)
        elif choice == "10":
            print(f"Выручка: {get_total_revenue(rentals):.2f} руб.")
        elif choice == "0":
            save_scooters(scooters)
            save_users(users)
            save_stations(stations)
            save_rentals(rentals)
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()