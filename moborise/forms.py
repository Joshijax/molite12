from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import uploads, Agent
 
class AgentForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'first-name' }))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Surname' }))
    email = forms.EmailField(max_length=254, label='email', help_text='Required. Inform a valid email address.', widget= forms.TextInput
                           (attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'input your password' }))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'confirm password' }))
    class Meta:
        model =Agent
        fields = ('firstname', 'lastname','email','password', 'password2')

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = Agent.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')

class LoginUpForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username' }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'input your password' }))
    

    class Meta:
        model = Agent
        fields = ('username' , 'password', )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name' }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name' }))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username' }))
    email = forms.EmailField(max_length=254, label='email', help_text='Required. Inform a valid email address.', widget= forms.TextInput
                           (attrs={'placeholder':'Email', 'type': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'input your password' }))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'confirm password' }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username' , 'email', 'password1', 'password2', )