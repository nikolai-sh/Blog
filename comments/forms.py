from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """ Class to create comment form """
    template_name = 'blog/post_detail.html'

    class Meta:
        model = Comment
        fields = ['body']