from rest_framework import serializers
from .models import User, DashboardInterface, CAPSCurriculumStructure, Assessment, AssessmentReport
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()

    class Meta:
        model = User
        fields = '__all__'

class DashboardInterfaceSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    members = UserSerializer(many=True)

    class Meta:
        model = DashboardInterface
        fields = '__all__'

class CAPSCurriculumStructureSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    user = ObjectIdField()

    class Meta:
        model = CAPSCurriculumStructure
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    user = UserSerializer()  # Expand the user object

    class Meta:
        model = Assessment
        fields = '__all__'

class AssessmentReportSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()

    class Meta:
        model = AssessmentReport
        fields = '__all__'