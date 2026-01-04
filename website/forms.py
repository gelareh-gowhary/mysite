from django import forms
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name=forms.CharField(max_length=255)
                   
class ContactForm(forms.ModelForm):
    captcha=CaptchaField()                  