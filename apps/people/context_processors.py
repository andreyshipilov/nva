from .models import Human


def add_random_human(request):
    slug = request.path.strip("/")
    humans = Human.objects.filter(page__slug=slug).order_by("?")

    return {
        "human": humans[0] if humans.exists() else Human.objects.none(),
    }
