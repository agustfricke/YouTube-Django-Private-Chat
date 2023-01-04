from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, ImageField, FileInput

from . models import User

class UpdateUserProfile(ModelForm):
    avatar = ImageField(widget=FileInput)
    class Meta:
        model = User
        fields = ['email', 'username', 'avatar']

    def __init__(self, *args, **kwargs):
        super(UpdateUserProfile, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'rounded-lg block w-full bg-gray-700 p-2 text-white'
        self.fields['username'].widget.attrs['class'] = 'rounded-lg block w-full bg-gray-700 p-2 text-white'
        self.fields['avatar'].widget.attrs['class'] = 'rounded-lg block w-full bg-gray-700 p-2 text-white'

        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['avatar'].widget.attrs['placeholder'] = 'Avatar'

    


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'rounded-lg block w-full bg-gray-700 p-2 text-white'
        self.fields['username'].widget.attrs['class'] = 'rounded-lg block w-full bg-gray-700 p-2 text-white'
        self.fields['password1'].widget.attrs['class'] = 'rounded-lg block w-full bg-gray-700 p-2 text-white'
        self.fields['password2'].widget.attrs['class'] = 'rounded-lg block w-full bg-gray-700 p-2 text-white'

        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
