from django.test import TestCase, Client
from django.urls import reverse
from .models import Team, OctofitUser, Activity, Workout


class BasicModelsTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Team Alpha', description='Test team')
        self.user = OctofitUser.objects.create(name='Alice', email='alice@example.com', team=self.team)

    def test_team_and_user_str(self):
        self.assertEqual(str(self.team), 'Team Alpha')
        self.assertIn('Alice', str(self.user))

    def test_activity_and_workout_creation(self):
        activity = Activity.objects.create(user=self.user, activity_type='run', distance_km=5.0, duration_minutes=30)
        workout = Workout.objects.create(title='Morning Run', description='Easy jog', duration_minutes=30, team=self.team)
        self.assertIn('run', str(activity))
        self.assertEqual(str(workout), 'Morning Run')


class ApiRootTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_api_root_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        # expect keys for main endpoints
        for key in ('teams', 'users', 'activities', 'leaderboard', 'workouts'):
            self.assertIn(key, data)
