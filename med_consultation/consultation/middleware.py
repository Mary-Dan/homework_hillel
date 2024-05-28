import time
from django.utils import timezone


class RequestTimeMiddleware:
    """Middleware для відстеження часу виконання запитів."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.start_time = time.time()
        response = self.get_response(request)
        request.end_time = time.time()
        return response

    def process_response(self, request, response):
        duration = request.end_time - request.start_time
        print(f"Request to {request.path} took {duration} seconds.")
        return response