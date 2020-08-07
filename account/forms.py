from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Repeat Password'
                                }))

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name')

        # add placeholder to django fields!
        widgets = {
            'email':forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),

            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username'
                }
            ),

            'first_name': forms.TextInput(
                attrs={
                    'placeholder':'Full Name'
                }
            )
        }

    def clean_password2(self):

        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')

        return cd['password2']