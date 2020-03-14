from django import forms
from rate_my_agency.models import Rating, Comment

class CommentForm(forms.ModelForm):
    commentText = forms.CharField(max_length = 300)



    
    
