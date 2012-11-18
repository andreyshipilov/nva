from .models import Human


def add_random_human(request):
    return {
        "human": Human.get_random(),
    }