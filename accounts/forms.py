from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
    }))
    confrim_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confrim Password',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone', 'email', 'password']

    def __init__(self,*args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter Your First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Your Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Your Email'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter Your Phone Number'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confrim_password = cleaned_data.get('confrim_password')

        if password != confrim_password:
            raise forms.ValidationError(
                "Password Does Not Match!"
            )