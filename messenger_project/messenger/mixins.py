from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse


# 1. Міксін для перевірки аутентифікації користувача
class AuthenticationMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)


# 2. Міксін для перенаправлення користувача
class RedirectMixin:
    def redirect_user(self, url):
        return HttpResponseRedirect(reverse(url))


# 3. Міксін для перевірки прав доступу користувача
class AuthorizationMixin:
    def has_permission(self, request):
        pass


# 4. Міксін для перевірки прав доступу користувача
class AuthorizationMixin:
    def has_permission(self, request):
        pass


# 5. Міксін для надання відповіді у форматі JSON
class JSONResponseMixin:
    def render_json_response(self, data):
        pass


# 6. Міксін для журналювання подій
class LoggingMixin:
    def log_event(self, event):
        pass


# 7. Міксін для відображення статичних шаблонів
class StaticTemplateMixin:
    template_name = 'static_template.html'


# 8. Міксін для отримання об'єктів (наприклад, чатів)
class ObjectFetchingMixin:
    def get_user_chats(self, user):
        pass


# 9. Міксін для обробки форм
class FormProcessingMixin:
    def process_form(self, form):
        pass


# 10. Міксін для валідації даних
class DataValidationMixin:
    def validate_data(self, data):
        pass