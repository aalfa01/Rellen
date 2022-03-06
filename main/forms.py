from django import forms
from .models import Ism

class ContactForm(forms.ModelForm):
  
  class Meta:
    model = Ism
    fields = ['name','phone','message']

    labels = {
      'name' : '',
      'phone' : '',
      'message' : ''
    }

    widgets = {
      'name': forms.TextInput(attrs = {
        'placeholder':'Ism...',
      }),
      'phone': forms.TextInput(attrs = {
        'placeholder':'+998()...',
      }),
      'message': forms.Textarea(attrs = {
        'placeholder':'Xabar...',
        'rows':'4'
      })
    }

    