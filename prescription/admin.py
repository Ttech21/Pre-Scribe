from django.contrib import admin
from .models import Profile,Prescription,Patient,Medicine,Advice,MedicineUsage,InitialExamination,Investigation,FileUpload
# Register your models here.

admin.site.register([Profile,Prescription,Patient,Medicine,Advice,MedicineUsage,InitialExamination,Investigation,FileUpload])