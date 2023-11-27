"""forms"""
from django import forms

class PhoneNumberForm(forms.Form):
    """class for phone number form"""
    phone_number = forms.CharField(label='Введите номер телефона', widget=forms.TextInput(attrs={'placeholder': '89998887766'}), required=True)

class CodeVerifForm(forms.Form):
    """form for verif"""
    verif_code = forms.CharField(label='Введите код авторизации', widget=forms.TextInput(attrs={'placeholder': 'Code'}), required=True)

class FriendCodeForm(forms.Form):
    """Friend code form"""
    phone_number = forms.CharField(label='Ввести код друга', widget=forms.TextInput(attrs={'placeholder': '1A2b3C'}), required=True)
    