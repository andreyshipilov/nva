from .models import Setup


def add_setup(request):
    return {
        "setup": Setup.get_available(),
    }
