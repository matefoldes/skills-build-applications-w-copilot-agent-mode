"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import TeamViewSet, OctofitUserViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'users', OctofitUserViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)


@api_view(['GET'])
def api_root(request, format=None):
    """Named API root for the project (used by tests and discoverability)."""
    # Prefer constructing URLs from the Codespace hostname when available so
    # external tools (like the Codespaces forwarded URL) get reachable links
    # without hard-coding the Codespace name. Fall back to the request host.
    codespace = os.environ.get('CODESPACE_NAME')
    if codespace:
        base = f"https://{codespace}-8000.app.github.dev"
    else:
        # Fallback to the request host/scheme
        base = request.build_absolute_uri('/')[:-1]  # remove trailing slash

    def api(path):
        return f"{base}/api/{path}/"

    return Response({
        'teams': api('teams'),
        'users': api('users'),
        'activities': api('activities'),
        'leaderboard': api('leaderboard'),
        'workouts': api('workouts'),
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # API root view at '/'
    path('', api_root),
]
