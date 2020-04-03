from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rate_my_agency.models import Comment, Agency, Tenant, City, Rating, Image


# Form for adding a comment to an agency's page
class CommentForm(forms.ModelForm):
    commentText = forms.CharField(max_length = 300,
                                  label="",
                                  widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ('commentText',)

# Form for creating a new user
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user

# Form for creating a new agency (when a new user is made)
class AgencyForm(forms.ModelForm):
    agencyName = forms.CharField(label = "Agency Name")
    cities = forms.ModelMultipleChoiceField(help_text = "(Control + left click to make a selection!)", queryset=City.objects.all())
    website = forms.URLField(label = "Website",required = False,)
    
    class Meta:
        model = Agency
        fields = ('agencyName', 'cities', 'website',)

# Form for creating a new agency (when a new user is made)
class TenantForm(forms.ModelForm):
    first_name = forms.CharField(max_length = 30, label="First name")
    last_name = forms.CharField(max_length = 30, label="Surname")
    class Meta:
        model = Tenant
        fields = ('first_name','last_name')

# Form for adding a picture to an agency's page, logged in as an agency
class PictureForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)





    
    
