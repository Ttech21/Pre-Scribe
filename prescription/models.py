import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='profile-pictures/', default='profile-pictures/user-default.png')
    degree = models.TextField(max_length=500, blank=True, null=True)
    speciality = models.CharField(max_length=100, blank=True, null=True)
    post = models.CharField(max_length=100, blank=True, null=True)
    hospital_name = models.CharField(max_length=100, blank=True, null=True)
    chamber = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    slug = models.SlugField(default="", blank=True, null=False, max_length=1000)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.user_name)
        super().save(*args,**kwargs)

    def __str__(self):
        return "Dr. "+str(self.name)

#################################################


class MedicineTypes(models.TextChoices):
    Tablet = 'Tablet', 'Tablet'
    Syrup = 'Syrup', 'Syrup'
    Injection = 'Injection', 'Injection'
    Saline = 'Saline','Saline'

class Medicine(models.Model):
    name = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    type = models.CharField(max_length=20,choices=MedicineTypes.choices)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name + " " + self.group + " " + self.type


class MedicineDose(models.TextChoices):
    EMPTY_LABEL = '', 'Dose'
    Option1 = '0+0+1','0+0+1'
    Option2 = '0+1+0','0+1+0'
    Option3 = '1+0+0','1+0+0'
    Option4 = '0+1+1','0+1+1'
    Option5 = '1+0+1','1+0+1'
    Option6 = '1+1+0','1+1+0'
    Option7 = '1+1+1','1+1+1'


class MedicineInstruction(models.TextChoices):
    EMPTY_LABEL = '', 'Select Condition'
    AfterMeal = 'After Meal','After Meal'
    BeforeMeal = 'Before Meal','Before Meal'


class MedicineDuration(models.TextChoices):
    EMPTY_LABEL = '', 'Duration '
    Option1 = '7 Days', '7 Days'
    Option2 = '10 Days', '10 Days'
    Option3 = '15 Days', '15 Days'
    Option4 = '20 Days', '20 Days'
    Option5 = '1 Days', '1 Month'





#########################################################


class Advice(models.Model):
    doctor = models.ForeignKey(Profile,on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Investigation(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)



class Gender(models.TextChoices):
    EMPTY_LABEL = '', 'Select Gender '
    Male = 'Male', 'Male'
    Female = 'Female', 'Female'
    Other = 'Other', 'Other'

class Patient(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    age = models.PositiveIntegerField(blank=True,null=True)
    gender = models.CharField(blank=True,null=True,choices=Gender.choices,max_length=10)
    phone_number = models.CharField(blank=True,null=True,max_length=20)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)




class InitialExamination(models.Model):
    pulse = models.PositiveIntegerField(blank=True,null=True)
    temperature = models.PositiveIntegerField(blank=True,null=True)
    bp_upper = models.PositiveIntegerField(blank=True,null=True)
    bp_lower = models.PositiveIntegerField(blank=True,null=True)


class Prescription(models.Model):
    doctor = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL)
    complaints = models.TextField(blank=True,null=True)
    diagnosis = models.TextField(blank=True,null=True)
    investigation = models.ManyToManyField(Investigation,blank=True)
    advice = models.ManyToManyField(Advice,blank=True)
    patient = models.ForeignKey(Patient,blank=True,null=True,on_delete=models.SET_NULL)
    initial_examination = models.ForeignKey(InitialExamination,blank=True,null=True,on_delete=models.SET_NULL)

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        if self.patient and self.patient.name:
            return self.patient.name
        else:
            return str(self.id)



class MedicineUsage(models.Model):
    prescription = models.ForeignKey(Prescription,blank=True,null=True,on_delete=models.SET_NULL)
    medicine = models.ForeignKey(Medicine,blank=True,null=True,on_delete=models.SET_NULL)
    dose = models.CharField(max_length=50,choices=MedicineDose.choices,blank=True,null=True)
    instruction = models.CharField(max_length=50,choices=MedicineInstruction.choices,blank=True,null=True)
    duration = models.CharField(max_length=50,choices=MedicineDuration.choices,blank=True,null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.id)
        # return self.dose + " " + self.instruction + " " + self.duration


# model for uploading csv/excel file for bulk create
class FileUpload(models.Model):
    file = models.FileField(upload_to='files/',validators=[FileExtensionValidator(['csv', 'xls', 'xlsx'])])
    used = models.BooleanField(default=False)

