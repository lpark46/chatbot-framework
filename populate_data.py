import os
import django
from datetime import datetime

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_framework.settings')
django.setup()

from kakao_app.models import Team, Subject, Test, Visit

# Data to be inserted
teams = [
    {"team_name": "TEAM1", "researcher": "Laura", "date": "2024-08-19", "time_start": "10:00", "time_end": "10:30", "max_capacity": 3},
    {"team_name": "TEAM2", "researcher": "John", "date": "2024-08-19", "time_start": "10:00", "time_end": "10:30", "max_capacity": 3},
    {"team_name": "TEAM3", "researcher": "Smith", "date": "2024-08-19", "time_start": "10:00", "time_end": "10:30", "max_capacity": 3}
]

subjects = [
    {"subject_name": "John Doe", "subject_contact": "123-456-7890"},
    {"subject_name": "Apeach", "subject_contact": "123-456-7890"},
    {"subject_name": "Lion", "subject_contact": "123-456-7890"}
]

tests = [
    {"test_name": "test A", "team_name": "TEAM1"},
    {"test_name": "test B", "team_name": "TEAM2"}
]

visits = [
    {"subject_name": "John Doe", "test_name": "test A", "visit_date": "2024-08-20", "time_start": "10:00", "time_end": "10:30", "group_id": "G1"},
    {"subject_name": "Apeach", "test_name": "test B", "visit_date": "2024-08-21", "time_start": "11:00", "time_end": "11:30", "group_id": "G2"},
    {"subject_name": "Lion", "test_name": "test A", "visit_date": "2024-08-22", "time_start": "12:00", "time_end": "12:30", "group_id": "G1"}
]

# Insert data into Team table
for team_data in teams:
    Team.objects.create(
        team_name=team_data["team_name"],
        researcher=team_data["researcher"],
        date=team_data["date"],
        time_start=team_data["time_start"],
        time_end=team_data["time_end"],
        max_capacity=team_data["max_capacity"]
    )

# Insert data into Subject table
for subject_data in subjects:
    Subject.objects.create(
        subject_name=subject_data["subject_name"],
        subject_contact=subject_data["subject_contact"]
    )

# Insert data into Test table
for test_data in tests:
    team = Team.objects.get(team_name=test_data["team_name"])
    Test.objects.create(
        test_name=test_data["test_name"],
        team=team
    )

# Insert data into Visit table
for visit_data in visits:
    subject = Subject.objects.get(subject_name=visit_data["subject_name"])
    test = Test.objects.get(test_name=visit_data["test_name"])
    Visit.objects.create(
        subject=subject,
        test=test,
        visit_date=visit_data["visit_date"],
        time_start=visit_data["time_start"],
        time_end=visit_data["time_end"],
        group_id=visit_data["group_id"]
    )

print("Data successfully inserted.")
