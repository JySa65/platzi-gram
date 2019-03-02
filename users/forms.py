from django import forms
from django.contrib.auth.forms import UserCreationForm as UserForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _
from users. models import Profile

class UserCreationForm(UserForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control', 
                'placeholder': ' '.join(name.split('_')).title()
            })

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
            raise forms.ValidationError(_("A user with this email already exists."))
        except User.DoesNotExist:
            pass
        return self.cleaned_data['email']


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        exclude = ('user',)
