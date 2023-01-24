from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm,Select

from .models import Prescription,MedicineUsage,Patient,Advice,FileUpload,Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username','email','password1','password2']
        labels = {
            'first_name':'Name',
        }

    # def __init__(self,*args,**kwargs):
    #     super(CustomUserCreationForm, self).__init__(*args,**kwargs)
    #     # self.fields['title'].widget.attrs.update({"class": "input input--text", "placeholder": "Give a Title"})
    #     for label,field in self.fields.items():
    #         field.widget.attrs.update({"class":"input input--text"})


class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = ['medicine','advice']

        widgets = {
            'medicine': Select(),
            'advice':Select()
        }


    def __init__(self,profile, *args,**kwargs,):
        super(PrescriptionForm, self).__init__(*args,**kwargs)
        if profile:
            self.fields['advice'].queryset = Advice.objects.filter(doctor=profile)


class MedicineUsageForm(ModelForm):
    class Meta:
        model = MedicineUsage
        fields = '__all__'


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class FileUploadForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file']