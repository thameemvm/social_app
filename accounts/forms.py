from django import forms 
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            # import pdb; pdb.set_trace()
            if not user:
                # raise forms.ValidationError('This user does not exists')
                self.add_error("username", 'Invalid Username or Password')
            if user:
                if not user.is_active:
                    # raise forms.ValidationError('This user is no longer active.')
                    self.add_error("username", 'Invalid Username or Password')
        return self.cleaned_data



class SignUpForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email:
            qs = User.objects.filter(email__iexact=email)
            if qs.exists():
                self.add_error("email", "This Email Id already existed.")
        return email

    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            self.add_error("password1", "Please enter the same password")

        self.cleaned_data