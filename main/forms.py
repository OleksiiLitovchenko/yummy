from django import forms
from .models import Reservation
class ReservationForm(forms.ModelForm):
    name = forms.CharField(label= 'name', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Your Name',
                                                                        'id': 'name',
                                                                        'data-rule': 'minlen:4',
                                                                        'data-msg':'Please enter at least 4 chars'}))
    email = forms.EmailField(label = 'email', widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                             'id':"email",
                                                                             "placeholder":"Your Email",
                                                                             "data-rule":"email",
                                                                             "data-msg":"Please enter a valid email"}))
    phone = forms.CharField(label = 'phone', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                           "id":"phone",
                                                                           "placeholder":"Your Phone",
                                                                           "data-rule":"minlen:4",
                                                                           "data-msg":"Please enter at least 4 chars"}))
    date = forms.DateField(label = 'date', widget=forms.DateInput(attrs={'class': 'form-control',
                                                                         'id':"date",
                                                                         'placeholder':"YYY-MM-DD",
                                                                         'data-rule':"minlen:4",
                                                                         'data-msg':"Please enter at least 4 chars"}))
    time = forms.TimeField(label = 'time', widget=forms.TimeInput(attrs={'class': 'form-control','id':"time",
                                                                         'placeholder':"HH:MM",
                                                                         'data-rule':"minlen:4",
                                                                         'data-msg':"Please enter at least 4 chars"}))
    people = forms.IntegerField(label = 'people', widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                                  'id':"people",
                                                                                  'placeholder':"# of people",
                                                                                  'data-rule':"minlen:1",
                                                                                  'data-msg':"Please enter at least 1 chars"}))
    message = forms.CharField(label = 'message', widget=forms.Textarea(attrs={
                                                                              'class':"form-control",
                                                                              'rows':"5",
                                                                              'placeholder':"Message"}))
    class Meta:
        model = Reservation
        fields = ('name','email','phone', 'date', 'people', 'message', 'time')

