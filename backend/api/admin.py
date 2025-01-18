from django.contrib import admin
from .models import Exercise, SystemUser, BrowsingHistory

admin.site.register(SystemUser)
admin.site.register(Exercise)
admin.site.register(BrowsingHistory)