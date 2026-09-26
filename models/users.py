"""Класс User и функции работы с пользователями."""

from typing import List, Optional


class User:
    """Пользователь системы."""

    def __init__(self, user_id: int, name: str, email: str) -> None:
        """Создать объект пользователя."""
        self.id = user_id
        self.name = name
        self.email = email

    def __str__(self) -> str:
        """Строковое представление пользователя."""
        return f"{self.name} <{self.email}>"

    @classmethod
    def from_data(cls, data: dict) -> "User":
        """Создать пользователя из набора данных."""
        return cls(
            user_id=data["id"],
            name=data["name"],
            email=data["email"],
        )

    def to_data(self) -> dict:
        """Преобразовать объект в данные для JSON."""
        return {"id": self.id, "name": self.name, "email": self.email}


def add_user(
    users: List[User],
    name: str,
    email: str,
) -> User:
    """Создать объект User и добавить его в коллекцию."""
    new_id = max((u.id for u in users), default=0) + 1
    user = User(new_id, name, email)
    users.append(user)
    return user


def find_user_by_id(
    users: List[User],
    user_id: int,
) -> Optional[User]:
    """Найти пользователя по идентификатору."""
    for u in users:
        if u.id == user_id:
            return u
    return None


def find_users(users: List[User], query: str) -> List[User]:
    """Найти пользователей по имени или email."""
    q = query.lower()
    return [
        u for u in users
        if q in u.name.lower() or q in u.email.lower()
    ]


def show_users(users: List[User]) -> None:
    """Вывести список пользователей."""
    if not users:
        print("Пользователей нет.")
        return
    for u in users:
        print(f"  [{u.id}] {u}")