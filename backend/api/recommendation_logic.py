from django.db.models import Count
from .models import BrowsingHistory, Exercise

def recommend_exercises(user):
    """
    Generuje rekomendacje ćwiczeń na podstawie historii przeglądania użytkownika.
    """
    most_viewed_groups = (
        BrowsingHistory.objects.filter(user=user)
        .values('exercise__muscle_group')
        .annotate(count=Count('exercise__muscle_group'))
        .order_by('-count')
    )

    if not most_viewed_groups:
        return Exercise.objects.none()

    top_group = most_viewed_groups[0]['exercise__muscle_group']
    return Exercise.objects.filter(muscle_group=top_group).exclude(
        id__in=BrowsingHistory.objects.filter(user=user).values_list('exercise_id', flat=True)
    )