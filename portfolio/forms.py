from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'subject'}
        ))
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={'class':'form-control', 'style':'height:250px; resize:none;','placeholder':'Message'}

        )
    )
    email_send = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'email'}
        ))

