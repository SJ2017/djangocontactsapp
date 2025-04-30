from django import forms
from .import models
from django.contrib.auth.models import User


class Form_one(forms.ModelForm):
    class Meta:
        model = models.contact
        # Explicitly list fields you want to include, excluding 'currentuser'
        fields = ['name', 'phno', 'email']  # Only show fields you want

    def save(self, commit=True):
        # Automatically associate the current logged-in user with the contact
        instance = super().save(commit=False)
        if commit:
            # Set the logged-in user as the 'currentuser' field
            instance.currentuser = self.user  # `self.user` should be set in the view
            instance.save()
        return instance

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ("username","password","email")
    
class UploadForm(forms.ModelForm):
    
    class Meta:
        model = models.Userprofileinfo
        fields = ("profilepic","portfoliosite")

