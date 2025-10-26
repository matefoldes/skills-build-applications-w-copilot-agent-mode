from django.core.management.base import BaseCommand
from django.utils import timezone

from octofit_tracker.models import Team, OctofitUser, Activity, Leaderboard, Workout

import pymongo


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Starting population of octofit_db...')

        # Delete existing data: drop collections directly via pymongo to avoid FK/PK mismatches
        try:
            client = pymongo.MongoClient('mongodb://localhost:27017')
            db = client['octofit_db']
            for col in ['leaderboard', 'activities', 'workouts', 'users', 'teams']:
                if col in db.list_collection_names():
                    db.drop_collection(col)
            self.stdout.write('Dropped existing collections (if any) to ensure a clean start.')
        except Exception as e:
            self.stderr.write(f'Warning: could not drop collections via pymongo: {e}')

        # Proceed with ORM insertion

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Team Marvel heroes')
        dc = Team.objects.create(name='dc', description='Team DC heroes')

        # Sample superhero users
        sample_users = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.test', 'team': marvel, 'is_superhero': True},
            {'name': 'Iron Man', 'email': 'ironman@marvel.test', 'team': marvel, 'is_superhero': True},
            {'name': 'Hulk', 'email': 'hulk@marvel.test', 'team': marvel, 'is_superhero': True},
            {'name': 'Superman', 'email': 'superman@dc.test', 'team': dc, 'is_superhero': True},
            {'name': 'Batman', 'email': 'batman@dc.test', 'team': dc, 'is_superhero': True},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.test', 'team': dc, 'is_superhero': True},
        ]

        users = []
        for u in sample_users:
            user = OctofitUser.objects.create(name=u['name'], email=u['email'], team=u['team'], is_superhero=u['is_superhero'])
            users.append(user)

        # Workouts
        Workout.objects.create(title='5K Run', description='Easy 5 kilometer run', duration_minutes=30, team=marvel)
        Workout.objects.create(title='HIIT Session', description='High intensity interval training', duration_minutes=45, team=dc)

        # Activities
        Activity.objects.create(user=users[0], activity_type='run', distance_km=5.0, duration_minutes=28.5)
        Activity.objects.create(user=users[1], activity_type='cycle', distance_km=20.0, duration_minutes=60)
        Activity.objects.create(user=users[3], activity_type='swim', distance_km=2.0, duration_minutes=50)

        # Leaderboard
        Leaderboard.objects.create(user=users[0], score=150, rank=1)
        Leaderboard.objects.create(user=users[1], score=120, rank=2)
        Leaderboard.objects.create(user=users[3], score=130, rank=3)

        self.stdout.write('Inserted sample teams, users, activities, leaderboards and workouts via ORM.')

        # Ensure unique index on users.email using pymongo directly
        try:
            client = pymongo.MongoClient('mongodb://localhost:27017')
            db = client['octofit_db']
            db.users.create_index([('email', pymongo.ASCENDING)], unique=True)
            self.stdout.write('Created unique index on users.email (if not already present).')
        except Exception as e:
            self.stderr.write(f'Warning: could not create unique index via pymongo: {e}')

        self.stdout.write('Population complete.')
