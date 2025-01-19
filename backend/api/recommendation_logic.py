from django.db.models import Count
from .models import BrowsingHistory, Exercise


def recommend_based_on_recent_activity(user):
    """
    Generuje rekomendacje na podstawie ostatnio przeglądanych ćwiczeń.
    """
    # Pobierz ostatnie 5 przeglądanych ćwiczeń
    recent_exercises = (
        BrowsingHistory.objects.filter(user=user)
        .order_by('-timestamp')
        .values_list('exercise_id', flat=True)[:5]
    )

    # Pobierz ćwiczenia z tych samych grup mięśniowych co ostatnio przeglądane
    recent_muscle_groups = Exercise.objects.filter(
        id__in=recent_exercises
    ).values_list('muscle_group', flat=True)

    recommended = Exercise.objects.filter(
        muscle_group__in=recent_muscle_groups
    ).exclude(
        id__in=recent_exercises
    )[:10]

    return recommended

def recommend_based_on_popularity(user):
    """
    Generuje rekomendacje na podstawie popularności ćwiczeń w systemie.
    """
    # Pobierz najczęściej przeglądane ćwiczenia
    popular_exercises = (
        BrowsingHistory.objects.values('exercise')
        .annotate(count=Count('exercise'))
        .order_by('-count')
        .values_list('exercise', flat=True)[:10]
    )

    # Usuń ćwiczenia już oglądane przez użytkownika
    user_history = BrowsingHistory.objects.filter(user=user).values_list('exercise_id', flat=True)
    recommended = Exercise.objects.filter(id__in=popular_exercises).exclude(id__in=user_history)

    return recommended

def recommend_exercises(user):
    """
    Łączy różne metody rekomendacji, aby zapewnić lepsze wyniki.
    """
    # Sprawdź, czy użytkownik ma historię przeglądania
    if BrowsingHistory.objects.filter(user=user).exists():
        return recommend_based_on_recent_activity(user)
    else:
        return recommend_based_on_popularity(user)
    
