from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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