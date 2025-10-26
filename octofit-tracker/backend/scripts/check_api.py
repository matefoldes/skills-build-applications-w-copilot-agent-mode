import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from django.test import Client

client = Client()

paths = ['/api/users/', '/api/teams/', '/api/activities/', '/api/leaderboard/', '/api/workouts/']

for p in paths:
    resp = client.get(p)
    print(p, resp.status_code)
