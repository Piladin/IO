# app/middleware.py
from .models import BrowsingHistory

class SaveBrowsingHistoryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated and 'exercise_id' in request.GET:
            BrowsingHistory.objects.create(user=request.user, exercise_id=request.GET['exercise_id'])
        return response
