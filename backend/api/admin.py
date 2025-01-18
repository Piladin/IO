from django.contrib import admin
from .models import Exercise, SystemUser

admin.site.register(SystemUser)
admin.site.register(Exercise)