from django.http import HttpResponse


def page(title, content):
    """Единый каркас HTML-страницы с Bootstrap 5.3."""
    bootstrap = (
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3"
        "/dist/css/bootstrap.min.css"
    )
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,
        initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="{bootstrap}">
</head>
<body>
    <nav class="nav">
        <a class="nav-link" href="/">Главная</a>
        <a class="nav-link" href="/scooters/">Самокаты</a>
        <a class="nav-link" href="/rentals/">Аренды</a>
    </nav>
    <main class="container">{content}</main>
</body>
</html>"""


def index(request):
    content = """
    <h1 class="display-4">Scooter Rental System</h1>
    <p class="lead">Сервис аренды электросамокатов.</p>
    <a href="/scooters/" class="btn btn-primary me-2">Самокаты</a>
    <a href="/rentals/" class="btn btn-secondary">Аренды</a>
    """
    return HttpResponse(page("Scooter Rental System", content))