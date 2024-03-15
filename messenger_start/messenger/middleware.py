import time
import logging

logger = logging.getLogger(__name__)

class RequestTimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.start_time = time.time()
        response = self.get_response(request)
        runtime = round(time.time() - request.start_time, 2)
        logger.info(f"Request: {request.method} {request.path} - Runtime: {runtime} seconds")
        return response

