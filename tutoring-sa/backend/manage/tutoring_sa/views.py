from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    UserSerializer,
    DashboardInterfaceSerializer,
    CAPSCurriculumStructureSerializer,
    AssessmentSerializer,
    AssessmentReportSerializer
)
from .models import User, DashboardInterface, CAPSCurriculumStructure, Assessment, AssessmentReport

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://upgraded-engine-x5w46j7vr57p3v49w-8000.app.github.dev/'
    return Response({
        'users': base_url + 'api/users/',
        'dashboard_interfaces': base_url + 'api/dashboard-interfaces/',
        'caps_curriculum_structures': base_url + 'api/caps-curriculum-structures/',
        'assessments': base_url + 'api/assessments/',
        'assessment_reports': base_url + 'api/assessment-reports/',
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DashboardInterfaceViewSet(viewsets.ModelViewSet):
    queryset = DashboardInterface.objects.all()
    serializer_class = DashboardInterfaceSerializer

class CAPSCurriculumStructureViewSet(viewsets.ModelViewSet):
    queryset = CAPSCurriculumStructure.objects.all()
    serializer_class = CAPSCurriculumStructureSerializer

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

class AssessmentReportViewSet(viewsets.ModelViewSet):
    queryset = AssessmentReport.objects.all()
    serializer_class = AssessmentReportSerializer