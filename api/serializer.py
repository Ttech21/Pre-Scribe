from rest_framework.serializers import ModelSerializer
from prescription.models import Medicine,MedicineUsage,Investigation,Advice


class MedicineSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'


class MedicineUsageSerializer(ModelSerializer):
    class Meta:
        model = MedicineUsage
        fields = '__all__'


class MedicineUsageViewSerializer(ModelSerializer):
    medicine = MedicineSerializer(many=False)
    class Meta:
        model = MedicineUsage
        fields = '__all__'


class AdviceSerializer(ModelSerializer):
    class Meta:
        model = Advice
        fields = '__all__'


class InvestigationSerializer(ModelSerializer):
    class Meta:
        model = Investigation
        fields = '__all__'