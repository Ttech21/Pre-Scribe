from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm,Select,TextInput,Textarea

from .models import Prescription,MedicineUsage,Patient,Advice,InitialExamination,FileUpload


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
        fields = ['complaints','diagnosis']


    def __init__(self, *args,**kwargs,):
        super(PrescriptionForm, self).__init__(*args,**kwargs)
        # if profile:
        #     self.fields['advice'].queryset = Advice.objects.filter(doctor=profile)

        self.fields['complaints'].widget.attrs.update({"id": "complaints"})
        self.fields['diagnosis'].widget.attrs.update({"id": "diagnosis"})
        # self.fields['investigation'].widget.attrs.update({"id": "investigation"})
        # self.fields['advice'].widget.attrs.update({"id": "advice"})
        # self.fields['duration'].widget.attrs.update({"id": "medicine-duration"})


class MedicineUsageForm(ModelForm):
    class Meta:
        model = MedicineUsage
        fields = "__all__"
        exclude = ['prescription',]
        widgets = {
            'medicine': TextInput(),
        }


    def __init__(self,*args,**kwargs):
        super(MedicineUsageForm, self).__init__(*args,**kwargs)
        self.fields['medicine'].widget.attrs.update({"id": "medicine"})
        self.fields['dose'].widget.attrs.update({"id": "medicine-dose"})
        self.fields['instruction'].widget.attrs.update({"id": "medicine-instruction"})
        self.fields['duration'].widget.attrs.update({"id": "medicine-duration"})


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super(PatientForm, self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update({"id": "patient-name"})
        self.fields['age'].widget.attrs.update({"id": "patient-age"})
        self.fields['phone_number'].widget.attrs.update({"id": "patient-phone"})


class InitialExaminationForm(ModelForm):
    class Meta:
        model = InitialExamination
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(InitialExaminationForm, self).__init__(*args, **kwargs)
        self.fields['pulse'].widget.attrs.update({"id": "pulse"})
        self.fields['temperature'].widget.attrs.update({"id": "temperature"})
        self.fields['bp_upper'].widget.attrs.update({"id": "bp_upper"})
        self.fields['bp_lower'].widget.attrs.update({"id": "bp_lower"})



class FileUploadForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file']