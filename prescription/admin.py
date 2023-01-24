from django.contrib import admin
from .models import Profile,Prescription,Medicine,Advice,FileUpload
# Register your models here.

admin.site.register([Profile,Prescription,Medicine,Advice,FileUpload])