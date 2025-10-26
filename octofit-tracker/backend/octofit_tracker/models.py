from django.db import models
from djongo import models as djongo_models


class Team(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class OctofitUser(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_superhero = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.name} <{self.email}>"


class Activity(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(OctofitUser, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    distance_km = models.FloatField(null=True, blank=True)
    duration_minutes = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.activity_type} by {self.user.name}"


class Leaderboard(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(OctofitUser, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.IntegerField(default=0)
    rank = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        return f"{self.user.name}: {self.score}"


class Workout(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration_minutes = models.IntegerField(null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='workouts')

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.title
