from django import forms
from .models import Post

"""

This is the form that. we create the post through it.

"""
class postCreateFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['url','body','tags']
        labels = {
            "body": "Caption",
            "tags": 'Category'
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows':3,'placeholder':'add a caption...', 'class':'font1 text-4xl'}),
            'url': forms.TextInput(attrs={'placeholder': 'Add url...'}),
            'tags': forms.CheckboxSelectMultiple(),
        }
        
        
        
class postEditFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['url','body','tags']
        labels = {
            "body": "Caption",
            "tags": 'Category'
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows':3,'placeholder':'add a caption...', 'class':'font1 text-4xl'}),
            'url': forms.TextInput(attrs={'placeholder': 'Add url...'}),
            'tags': forms.CheckboxSelectMultiple(),
        }