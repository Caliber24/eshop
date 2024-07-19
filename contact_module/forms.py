from django import forms
from django.core import validators
from .models import Contact



class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        max_length=50,
        error_messages={
            'required': 'لطفا نام‌ونام‌خانوادگی خود را وارد کنید',
            'max_length': 'نام و نام خانوادگی نمیتواند بالای 50کاراکتر باشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام و نام خانوادگی'
        })
    )
    email = forms.EmailField(label='ایمیل',
         widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل'
         }))

    title = forms.CharField(label='عنوان',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'عنوان'
        }))

    message = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'متن',
    }), label='متن پیام')


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'title', 'message']
        # fields = '__all__' #hame ro miyare
        # exclude = ['response']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'}),
            'email': forms.TextInput(attrs={
                'class': 'form-control'}),
            'title': forms.TextInput(attrs={
                'class': 'form-control'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message'
            })
        }
        labels = {
            'full_name': 'نام و نام خانوادگی شما',
            'email': 'ایمیل شما'
        }

        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادگی اجباری میباشد لطفا وارد کنید  '
            }
        }


class ProfileForm(forms.Form):
    user_image = forms.ImageField()
