"""Тесты класса User."""

from models import User
from models.users import add_user, find_user_by_id, find_users


def test_user_creation():
    u = User(1, "Иван Петров", "ivan@example.com")
    assert u.id == 1
    assert u.name == "Иван Петров"
    assert u.email == "ivan@example.com"


def test_user_from_data():
    data = {"id": 5, "name": "Анна", "email": "a@b.c"}
    u = User.from_data(data)
    assert u.id == 5
    assert u.name == "Анна"
    assert u.email == "a@b.c"


def test_add_user():
    users = []
    u = add_user(users, "Иван", "i@e.com")
    assert u.id == 1
    assert len(users) == 1


def test_find_user_by_id():
    users = []
    add_user(users, "Иван", "i@e.com")
    assert find_user_by_id(users, 1) is not None
    assert find_user_by_id(users, 99) is None


def test_find_users():
    users = []
    add_user(users, "Иван", "ivan@example.com")
    add_user(users, "Анна", "anna@example.com")
    assert len(find_users(users, "анна")) == 1