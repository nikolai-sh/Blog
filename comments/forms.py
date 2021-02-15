from django import forms
from django.contrib.messages.api import success
from .models import Comment

class CommentForm(forms.ModelForm):
    """ Class to create comment form """
   
    class Meta:
        model = Comment
        fields = ['author', 'text']