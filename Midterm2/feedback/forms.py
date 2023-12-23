from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['username', 'email', 'message']
        widgets = {
            'mesage': forms.Textarea(attrs={'rows': 4}),
        }