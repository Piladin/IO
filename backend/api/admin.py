from django.contrib import admin
from api.models.system_user import SystemUser
from api.models.exercise import Exercise
from api.models.browsing_history import BrowsingHistory

admin.site.register(SystemUser)
admin.site.register(Exercise)
admin.site.register(BrowsingHistory)