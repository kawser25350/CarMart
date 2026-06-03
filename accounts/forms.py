from django import forms
from djagno.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.model import User

class UserRegisterForm(UserCreationForm):
    date_of_birth=forms.DateInput(widget=forms.DateInput(attrs={'type':'date'}))
    phone=forms.CharField(max_length=11)
    address=forms.CharField(max_length=150)

    model=User

    # fields=['username','first_name','last_name','date_of_birth','address','email','phone']

    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'date_of_birth',
        'phone',
        'address',
        'password1',
        'password2'
    ]

    def save(self,commit=True):
        user=super.save(commit=False)

        if commit:
            user.save()

            Account.objects.create(
                user=user,
                date_of_birth=self.cleaned_data['date_of_birth'],
                phone=self.cleaned_data['phone'],
                address=self.cleaned_data['address']
            )

        return user
    




    
