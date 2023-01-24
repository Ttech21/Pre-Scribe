from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm,PrescriptionForm,MedicineUsageForm,PatientForm,FileUploadForm
from django.contrib.auth.models import User
from .models import Medicine,MedicineTypes,FileUpload
import csv
# Create your views here.


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            try:
                User.objects.get(username=user.username)
                form = CustomUserCreationForm(request.POST)
                context = {
                    'page': page,
                    'form': form
                }
                return render(request,'prescription/login-register.html', context)
            except ObjectDoesNotExist:
                user.save()
                login(request,user)
                return redirect('login')
        else:
            form = CustomUserCreationForm(request.POST)
            context = {
                'page': page,
                'form': form
            }
            return render(request, 'prescription/login-register.html', context)
    context={
        'page':page,
        'form':form
    }
    return render(request,'prescription/login-register.html',context)


def login_user(request):
    page = 'login'
    # if request.user.is_authenticated:
    #     return redirect('login')
    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            return redirect('login')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("login")
        else:
            return redirect('login')
    context={
        'page':page
    }
    return render(request,'prescription/login-register.html',context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')


def profile(request):
    choices = MedicineTypes.choices

    form = FileUploadForm()
    if request.method == "POST":
        form = FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            obj = FileUpload.objects.get(used=False)
            with open(obj.file.path, 'r',) as f:
                reader = csv.reader(f)
                for i,row in enumerate(reader):
                    if i==0:
                        pass
                    else:

                        name = row[0]
                        group = row[1]
                        type = row[2]

                        if type in choices:
                            index = choices.index(type)
                        else:
                            index=0
                        Medicine.objects.create(
                            name=name,
                            group =group,
                            type = MedicineTypes("Tablet")
                        )
                obj.used =True
                obj.save()


    context={
        'form':form
    }
    return render(request,'prescription/profile.html',context)

@login_required(login_url='login')
def prescription_create(request):
    user = request.user
    doctor = user.profile
    prescription_form = PrescriptionForm(profile=doctor)
    medicine_usage_form = MedicineUsageForm()
    patient_form = PatientForm()

    if request.method == 'POST':
        prescription_form = PrescriptionForm(doctor,request.POST,prefix='prescription')
        medicine_usage_form = MedicineUsageForm(request.POST,prefix='medicineusage')
        patient_form = PatientForm(request.POST,prefix='patient')

        if prescription_form.is_valid() and medicine_usage_form.is_valid() and patient_form.is_valid():
            prescription = prescription_form.save(commit=False)
            medicine_usage = medicine_usage_form.save()
            patient = patient_form.save()
            prescription.doctor = doctor
            prescription.patient = patient
            prescription.medicine_usage = medicine_usage
            prescription.save()


    context={
        'prescription_form':prescription_form,
        'medicine_usage_form':medicine_usage_form,
        'patient_form': patient_form,
    }

    return render(request,'prescription/prescription-create.html',context)

