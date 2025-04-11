from django.test import TestCase
from .models import User, DashboardInterface, CAPSCurriculumStructure, Assessment, AssessmentReport

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "testuser@example.com")

class DashboardInterfaceModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        self.dashboard = DashboardInterface.objects.create(name="Test Dashboard")
        self.dashboard.members.add(self.user)

    def test_dashboard_creation(self):
        self.assertEqual(self.dashboard.name, "Test Dashboard")
        self.assertIn(self.user, self.dashboard.members.all())

class CAPSCurriculumStructureModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        self.curriculum = CAPSCurriculumStructure.objects.create(user=self.user, curriculum_type="Math", duration="01:00:00")

    def test_curriculum_creation(self):
        self.assertEqual(self.curriculum.curriculum_type, "Math")
        self.assertEqual(self.curriculum.user, self.user)

class AssessmentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        self.assessment = Assessment.objects.create(user=self.user, score=95)

    def test_assessment_creation(self):
        self.assertEqual(self.assessment.score, 95)
        self.assertEqual(self.assessment.user, self.user)

class AssessmentReportModelTest(TestCase):
    def setUp(self):
        self.report = AssessmentReport.objects.create(name="Test Report", description="This is a test report.")

    def test_report_creation(self):
        self.assertEqual(self.report.name, "Test Report")
        self.assertEqual(self.report.description, "This is a test report.")