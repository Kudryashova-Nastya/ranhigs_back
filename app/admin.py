from django.contrib import admin
from app.models import Session, Team
from django.utils.dateformat import format


class SessionAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'teamCount', 'link', 'datetimeStart', 'status')
    search_fields = ('name',)
    list_filter = ('teamCount', 'status')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'userCount', 'pincode', 'sessionID')
    search_fields = ('name',)
    list_filter = ('userCount', 'sessionID')


admin.site.register(Session, SessionAdmin)
admin.site.register(Team, TeamAdmin)
