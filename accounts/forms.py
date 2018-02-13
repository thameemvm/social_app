from django import forms 
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
   					widget=forms.TextInput(
    						attrs={
				    				"class":"form-control form-control-solid placeholder-no-fix form-group",
				    				"placeholder":"Username",
				    				 "id":"username"
				    			}
				    		)
    					)
    password = forms.CharField(
    					widget=forms.PasswordInput(
							attrs={
								"class":"form-control form-control-solid placeholder-no-fix form-group",
								 "autocomplete":"off",
								 "placeholder":"Password",
								 "id":"password",
								  "name":"password"
							}
    							)
    						)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            # import pdb; pdb.set_trace()
            if not user:
                # raise forms.ValidationError('This user does not exists')
                raise forms.ValidationError('Invalid Username or Password')

            if not user.check_password(password):
                # raise forms.ValidationError('Incorrect password')
                raise forms.ValidationError('Invalid Username or Password')

            if not user.is_active:
                # raise forms.ValidationError('This user is no longer active.')
                raise forms.ValidationError('Invalid Username or Password')
        return self.cleaned_data