from django import forms
from .models import Link,Review

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('name','url',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full mt-2 py-4 px-6 bg-slate-100 border border-slate-300'}),
            'url': forms.URLInput(attrs={'class': 'w-full mt-2 py-4 px-6 bg-slate-100 border border-slate-300'})
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'content',)
        widgets = {
            'rating': forms.NumberInput(attrs={'class': 'w-full mt-2 py-4 px-6 bg-slate-100 border border-slate-300'}),
            'content': forms.Textarea(attrs={'class': 'w-full mt-2 py-4 px-6 bg-slate-100 border border-slate-300'})
        }