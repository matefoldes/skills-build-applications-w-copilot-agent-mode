from rest_framework import serializers
from .models import Team, OctofitUser, Activity, Leaderboard, Workout


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'name', 'description']

    def get_id(self, obj):
        return str(obj.pk) if obj and obj.pk is not None else None


class OctofitUserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()

    class Meta:
        model = OctofitUser
        fields = ['id', 'name', 'email', 'is_superhero', 'team']

    def get_id(self, obj):
        return str(obj.pk) if obj and obj.pk is not None else None

    def get_team(self, obj):
        team_id = getattr(obj, 'team_id', None)
        return str(team_id) if team_id else None


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'distance_km', 'duration_minutes', 'timestamp']

    def get_id(self, obj):
        return str(obj.pk) if obj and obj.pk is not None else None

    def get_user(self, obj):
        user_id = getattr(obj, 'user_id', None)
        return str(user_id) if user_id else None


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'score', 'rank']

    def get_id(self, obj):
        return str(obj.pk) if obj and obj.pk is not None else None

    def get_user(self, obj):
        user_id = getattr(obj, 'user_id', None)
        return str(user_id) if user_id else None


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ['id', 'title', 'description', 'duration_minutes', 'team']

    def get_id(self, obj):
        return str(obj.pk) if obj and obj.pk is not None else None

    def get_team(self, obj):
        team_id = getattr(obj, 'team_id', None)
        return str(team_id) if team_id else None
