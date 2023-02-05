from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from prescription.models import MedicineUsage,Medicine,Advice,Investigation
from .serializer import MedicineUsageSerializer,MedicineSerializer,MedicineUsageViewSerializer,AdviceSerializer,InvestigationSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_medicine(request):
    serializer = MedicineUsageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        obj = MedicineUsage.objects.get(id=serializer.data['id'])
        s = MedicineUsageViewSerializer(obj,many=False)
        return Response(s.data)
    return Response(serializer.data)


@api_view(['GET'])
def all_medicine(request):
    medicine =  Medicine.objects.all()
    serializer = MedicineSerializer(medicine, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def all_advice(request):
    advices =  Advice.objects.filter(doctor=request.user.profile)
    serializer = AdviceSerializer(advices,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def all_investigation(request):
    advices =  Investigation.objects.all()
    serializer = InvestigationSerializer(advices,many=True)
    return Response(serializer.data)



