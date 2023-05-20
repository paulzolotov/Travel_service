from django.shortcuts import redirect, reverse


class RedirectIfLoggedInMiddleware:
    """Класс-middleware, суть которого не давать авторизованному пользователю переходить на url /users/login/.
    Т.е если пользователь вошел в систему -> перенаправляем его на главную станицу"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path == "/users/login/":
            return redirect(reverse("booking:index"))
        return self.get_response(request)
