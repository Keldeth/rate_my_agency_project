from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from rate_my_agency.models import Comment, User, Agency, Tenant, City


class CommentForm(forms.ModelForm):
    commentText = forms.CharField(max_length = 300)


class AgencyForm(UserCreationForm):
    username = forms.CharField(label = "Username", max_length = 30, help_text = "Required. 30 characters or less")
    name = forms.CharField(label = "Agency Name")
    city = forms.ModelChoiceField(queryset=City.objects.all())
    url = forms.URLField(label = "Website",required = False,)
    
    
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'name', 'city','url')
    
          
class TenantForm(UserCreationForm):
    username = forms.CharField(label = "Username", max_length = 30, help_text = "Required. 30 characters or less")
   
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'name')


        





    
    
