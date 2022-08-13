from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=50)
    message = forms.CharField(max_length=1000)


class Subs(forms.Form):
    email = forms.EmailField()


class logistic(forms.Form):
    location = forms.CharField(max_length=220)
    to_destination = forms.CharField(max_length=220)
    email = forms.EmailField()
    number = forms.CharField(max_length=100)

