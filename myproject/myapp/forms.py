from django import forms
import datetime

class UserForm(forms.Form):
    name = forms.CharField(max_length = 20)
    transient_type = forms.CharField(max_length = 200, required=False)
    obs_or_lim = forms.ChoiceField(choices=[('o', 'observation'), ('l', 'limit')])
    DataTime = forms.DateTimeField(initial=datetime.date.today)
    Ra = forms.FloatField(required=False)
    Dec = forms.FloatField(required=False)
    max_limit = forms.IntegerField(required=False)
    max_magnitude = forms.IntegerField(required=False)
    lightcurve = forms.CharField(max_length = 300, required=False)
    pictures = forms.ImageField(required=False)
    telescope = forms.CharField(max_length = 30, required=False)
    publication = forms.CharField(max_length = 300, required=False)
    if_we_first = forms.ChoiceField(choices=[(True, 'yes'), (False, 'no')])
    time_from_notice = forms.IntegerField(required=False)
    satellite = forms.CharField(required=False)
    discoverer = forms.CharField(max_length = 30, required=False)

class UserRequest(forms.Form):    
    transient_type = forms.CharField(max_length = 200, required=False)
    obs_or_lim = forms.ChoiceField(choices=[('o', 'observation'), ('l', 'limit'), ('m', 'does not matter')])
    DataTime = forms.DateTimeField(initial=datetime.date.today)
    telescope = forms.CharField(max_length = 30, required=False)
    publication = forms.CharField(max_length = 300, required=False)
    if_we_first = forms.ChoiceField(choices=[(True, 'yes'), (False, 'no'), ('m', 'does not matter')])
    satellite = forms.CharField(required=False)
    discoverer = forms.CharField(max_length = 30, required=False)

class UserName(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 20)

class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Ваш email', required=True)
    subject = forms.CharField(label='Тема', required=True)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)

class Spinar(forms.Form):
    m = forms.FloatField()
    ao = forms.FloatField()
    am = forms.FloatField()