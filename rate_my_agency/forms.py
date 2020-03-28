from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from rate_my_agency.models import Comment, User, Agency, Tenant, City


class CommentForm(forms.ModelForm):
    commentText = forms.CharField(max_length = 300)


class AgencyForm(UserCreationForm):
    city = forms.ModelChoiceField(queryset=City.objects.all())
    url = forms.URLField(required = False)
    
    
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'city', 'url')
    
          
class TenantForm(UserCreationForm):
   
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)


        





    
    
