from django.contrib import admin
from .models import User, DashboardInterface, CAPSCurriculumStructure, Assessment, AssessmentReport

admin.site.register(User)
admin.site.register(DashboardInterface)
admin.site.register(CAPSCurriculumStructure)
admin.site.register(Assessment)
admin.site.register(AssessmentReport)