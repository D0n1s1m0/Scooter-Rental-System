from django.http import HttpResponse

from homepage.views import page
from models.scooters import find_scooter_by_id
from storage import load_scooters


def scooters(request):
    items = ""
    for s in load_scooters("data/scooters.json"):
        text = f"{s.model} — заряд {s.charge}%"
        items += f'<li class="list-group-item">{text}</li>'
    content = f"""
    <h1>Самокаты</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Самокаты", content))


def scooter_detail(request, scooter_id):
    scooters_list = load_scooters("data/scooters.json")
    scooter = find_scooter_by_id(scooters_list, scooter_id)
    if scooter is None:
        content = """
        <h1 class="text-danger">Самокат не найден</h1>
        <a href="/scooters/" class="btn btn-outline-secondary">
            ← к списку самокатов
        </a>
        """
        return HttpResponse(
            page("Самокат не найден", content), status=404,
        )
    available = scooter.is_available()
    status = "доступен" if available else "занят"
    badge = "bg-success" if available else "bg-danger"
    content = f"""
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{scooter.model}</h5>
        <p class="card-text"><strong>ID:</strong> {scooter.id}</p>
        <p class="card-text">
            <strong>Заряд:</strong> {scooter.charge}%
        </p>
        <p class="card-text">
            Статус: <span class="badge {badge}">{status}</span>
        </p>
        <a href="/scooters/" class="btn btn-outline-secondary">
            ← к списку самокатов
        </a>
      </div>
    </div>
    """
    return HttpResponse(page(scooter.model, content))