from django.contrib import admin
from .models import Team, OctofitUser, Activity, Leaderboard, Workout


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(OctofitUser)
class OctofitUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'team', 'is_superhero')
    search_fields = ('name', 'email')
    list_filter = ('is_superhero',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'user', 'distance_km', 'duration_minutes', 'timestamp')
    search_fields = ('activity_type',)


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'rank')
    ordering = ('-score',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'team', 'duration_minutes')
    search_fields = ('title',)
