from django import forms
from dreamapp.models import Message, Member, NewUser, Payment, Rating


class LoginForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'