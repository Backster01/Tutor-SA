from django.core.management.base import BaseCommand
from tutoring_sa.models import User, DashboardInterface, CAPSCurriculumStructure, Assessment, AssessmentReport
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, Dashboard interfaces, CAPS curriculum structure, assessments, and assessment reports'

    def handle(self, *args, **kwargs):
        # Create users
        users = [
            User(_id=ObjectId(), username='john_doe', email='john@example.com', password='password123'),
            User(_id=ObjectId(), username='jane_doe', email='jane@example.com', password='password123'),
        ]
        User.objects.bulk_create(users)

        # Create Dashboard interfaces
        dashboard = DashboardInterface(_id=ObjectId(), name='Main Dashboard')
        dashboard.save()
        dashboard.members.add(*users)

        # Create CAPS curriculum structures
        caps_curriculums = [
            CAPSCurriculumStructure(_id=ObjectId(), user=users[0], curriculum_type='Math', duration=timedelta(hours=1)),
            CAPSCurriculumStructure(_id=ObjectId(), user=users[1], curriculum_type='Science', duration=timedelta(hours=1, minutes=30)),
        ]
        CAPSCurriculumStructure.objects.bulk_create(caps_curriculums)

        # Create assessments
        assessments = [
            Assessment(_id=ObjectId(), user=users[0], score=85),
            Assessment(_id=ObjectId(), user=users[1], score=90),
        ]
        Assessment.objects.bulk_create(assessments)

        # Create assessment reports
        reports = [
            AssessmentReport(_id=ObjectId(), name='Midterm Report', description='Midterm performance review'),
            AssessmentReport(_id=ObjectId(), name='Final Report', description='Final performance review'),
        ]
        AssessmentReport.objects.bulk_create(reports)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))