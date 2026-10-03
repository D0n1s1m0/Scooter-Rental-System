from django.http import HttpResponse

from homepage.views import page
from models.rentals import find_rental_by_id
from storage import load_rentals, load_scooters, load_users


def rentals(request):
    scooters_list = load_scooters("data/scooters.json")
    users_list = load_users("data/users.json")
    rentals_list = load_rentals(
        scooters_list, users_list, "data/rentals.json",
    )
    items = ""
    for r in rentals_list:
        status = "завершена" if r.is_finished else "активна"
        badge = "bg-secondary" if r.is_finished else "bg-success"
        items += f"""
        <li class="list-group-item d-flex justify-content-between">
          <a href="/rentals/{r.id}/">
            {r.scooter.model} — {r.rental_date}
          </a>
          <span class="badge {badge}">{status}</span>
        </li>
        """
    content = f"""
    <h1>Аренды</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Аренды", content))


def rental_detail(request, rental_id):
    scooters_list = load_scooters("data/scooters.json")
    users_list = load_users("data/users.json")
    rentals_list = load_rentals(
        scooters_list, users_list, "data/rentals.json",
    )
    rental = find_rental_by_id(rentals_list, rental_id)
    if rental is None:
        content = """
        <h1 class="text-danger">Аренда не найдена</h1>
        <a href="/rentals/" class="btn btn-outline-secondary">
            ← к списку аренд
        </a>
        """
        return HttpResponse(
            page("Аренда не найдена", content), status=404,
        )
    status = "завершена" if rental.is_finished else "активна"
    badge = "bg-secondary" if rental.is_finished else "bg-success"
    content = f"""
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Аренда №{rental.id}</h5>
        <p class="card-text">
            Самокат: {rental.scooter.model}
        </p>
        <p class="card-text">Дата: {rental.rental_date}</p>
        <p class="card-text">Пользователь: {rental.user.name}</p>
        <p class="card-text">
            Статус: <span class="badge {badge}">{status}</span>
        </p>
        <a href="/rentals/" class="btn btn-outline-secondary">
            ← к списку аренд
        </a>
      </div>
    </div>
    """
    return HttpResponse(page(f"Аренда №{rental.id}", content))