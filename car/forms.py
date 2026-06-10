from django import forms
from .models import Comment,Car

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        
class CarForm(forms.ModelForm):
    class Meta:
        model=Car
        fields="__all__"
        
