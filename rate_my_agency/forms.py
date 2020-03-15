from django import forms
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm
from rate_my_agency.models import Comment, User

class CommentForm(forms.ModelForm):
    commentText = forms.CharField(max_length = 300)

class AgencyForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.user_type = 2
        if commit:
            user.save()
        return user

class TenantForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model = User

    
    def save(self):
        user = super().save(commit=False)
        user.user_type = 1
        user.save()
        tenant = Tenant.objects.create(user=user)
        return user
        
    
        

"""
class AgencyProfileForm(forms.ModelForm):
    class Meta:
        model = AgencyProfile
        fields = ('agency', 'url')
"""
        
    



    
    
