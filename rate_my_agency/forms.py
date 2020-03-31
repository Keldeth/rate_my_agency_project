from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rate_my_agency.models import Comment, Agency, Tenant, City


class CommentForm(forms.ModelForm):
    commentText = forms.CharField(max_length = 300)



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email',)


class AgencyForm(forms.ModelForm):
    agencyName = forms.CharField(label = "Agency Name")
    cities = forms.ModelMultipleChoiceField(queryset=City.objects.all())
    url = forms.URLField(label = "Website",required = False,)
    
    class Meta:
        model = Agency
        fields = ('agencyName', 'cities', 'url')
    
          
class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ()
        


        





    
    
