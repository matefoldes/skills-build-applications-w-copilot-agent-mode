---
mode: 'agent'
model: 'gpt-4.1'
---

# Django App Updates

- All Django project files are in the `octofit-tracker/backend/octofit_tracker` directory.

1. Update `settings.py` for MongoDB connection and CORS.
2. Update `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py`, and `admin.py` to support users, teams, activities, leaderboard, and workouts collections.
3. Ensure `/` points to the api and `api_root` is present in `urls.py`.

Notes for the agent:

- Follow existing code style and keep changes minimal and focused to the files listed above.
- Use Django ORM and project conventions already present in `octofit-tracker/backend/octofit_tracker`.
- After making changes, run the project's tests (if present) and ensure no syntax errors are introduced.
- Commit changes to branch `build-octofit-app` and describe the edits in the commit message.


```prompt
/update-octofit-tracker-app
```
