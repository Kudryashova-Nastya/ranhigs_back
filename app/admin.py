from django.contrib import admin

from app.models import Session, StatusSession, Team


admin.site.register(Session)
admin.site.register(StatusSession)
admin.site.register(Team)
