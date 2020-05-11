from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Agentuploads
from moborise.models import ProfilPicx, UserType
Property_type= [
    ('One room', 'One room'),
    ('Self Contain', 'Self Contain'),
    ('2 Bedroom', '2 Bedroom'),
    ('3 Bedroom', '3 Bedroom'),
    ]
Location= [
    ('Benin', 'Benin'),
    ('Lagos', 'Lagos'),
    ('Delta', 'Delta'),
   
    ]

propertyy_Location= [
    ('BDPA', 'BDPA'),
    ('Ekosodin', 'Ekosodin'),
    ('Osasoge', 'Osasoge'),
   
    ]

INTEGER_CHOICES= [tuple([x,x]) for x in range(1,500)]

class ProfileUploadForm(forms.Form):
    
    img = forms.FileField(widget=forms.ClearableFileInput(attrs={'placeholder':'input your password', 'class': 'custom-file-input',  'oninput' : 'input_filename();',  }))
    
    


class AgentUploadFileForm(forms.ModelForm):
    
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'placeholder':'input your password', 'class': 'upload-input',   'oninput' : 'input_filename();','multiple': 'multiple', 'accept' : 'image/jpg, image/gif/png, image/jpeg', }))

    
    property_Address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name of Address' }))
    property_Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name of Property' }))
    property_Location = forms.CharField(widget=forms.Select(choices=propertyy_Location))
    property_Description = forms.CharField(label='Describe the Property', widget=forms.Textarea(attrs={"rows":5, "cols":35 ,'placeholder':'About the property'}))
    property_Type = forms.CharField(label='Type of Property', widget=forms.Select(choices=Property_type))
    prize = forms.IntegerField(label='Amount to rent', widget=forms.Select(choices=INTEGER_CHOICES))

    

    def form_valid(self, form):
         obj = form.save(commit=False)
         if self.request.FILES:
            for f in self.request.FILES.getlist('file'):
                obj = self.model.objects.create(file=f)
                
                return super(AgentUploadFileForm, self).form_valid(form)



    
    class Meta:
        model = Agentuploads
        fields = ('file' ,'property_Name', 'property_Location', 'property_Description', 'property_Type', 'prize')




class AgentSignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name' }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name' }))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username' }))
    email = forms.EmailField(max_length=254, label='email', help_text='Required. Inform a valid email address.', widget= forms.TextInput
                           (attrs={'placeholder':'Email'}))
    Location = forms.CharField(label='Type of Property', widget=forms.Select(choices=Location))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'input your password' }))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'confirm password' }))

    

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username' , 'email', 'password1', 'password2', )
        
class AgentLoginUpForm(AuthenticationForm):
    username2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username ..' }))
    
    Loginpassword = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':' password' }))
    

    class Meta:
        model = User
        fields = ('username' , 'password', )
