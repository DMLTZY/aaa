from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField
from django import forms
from .models import MyUser


def _clean_mobile(value):
    try:
        value = int(value)
    except Exception as e:
        # print(e)
        raise forms.ValidationError(
            'Not a number, please enter a correct mobile number.',
            code='mobile_wrong',
        )

    if not (13000000000 < value < 20000000000):
        raise forms.ValidationError(
            'Please enter a correct mobile number.',
            code='mobile_wrong',
        )
    return value


class MyUserCreationForm(UserCreationForm):
    # mobile = forms.CharField(max_length=11)

    def clean_mobile(self):
        value = self.cleaned_data['mobile']
        return _clean_mobile(value)

    class Meta:
        model = MyUser
        fields = ("username", 'mobile', 'email', 'password1', 'password2')
        field_classes = {'username': UsernameField}

    # def save(self, commit=True):
    #     user = super(MyUserCreationForm, self).save(commit=False)
    #     user.mobile = self.cleaned_data["mobile"]
    #     if commit:
    #         user.save()
    #     return user


class MyUserChangeForm(UserChangeForm):
    # mobile = forms.CharField(max_length=11)

    def clean_mobile(self):
        value = self.cleaned_data['mobile']
        return _clean_mobile(value)

    class Meta:
        model = MyUser
        fields = '__all__'
        field_classes = {'username': UsernameField}


# class RegistrationForm(MyUserCreationForm):
#
#     class Meta(MyUserCreationForm.Meta):
#         pass

class RegistrationForm(MyUserCreationForm):

    class Meta:
        model = MyUser
        fields = ("username", 'mobile', 'email', 'password1', 'password2')
        field_classes = {'username': UsernameField}
        # model = MyUser
        # fields = ('username', 'mobile', 'email', 'password1', 'password2')
        # widgets = {
        #     'username': forms.TextInput(attrs={'placeholder': 'username', 'class': 'form-control top'}),
        #     'mobile': forms.TextInput(attrs={'placeholder': 'mobile', 'class': 'form-control middle'}),
        #     'email': forms.EmailInput(attrs={'placeholder': 'mail@domain.com', 'class': 'form-control middle'}),
        #     'password1': forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'form-control middle'}),
        #     'password2': forms.PasswordInput(attrs={'placeholder': 're-password', 'class': 'form-control bottom'}),
        # }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'username', 'class': 'form-control top'})
        self.fields['mobile'].widget = forms.TextInput(attrs={'placeholder': 'mobile', 'class': 'form-control middle'})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'mail@domain.com', 'class': 'form-control middle'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'form-control middle'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 're-password', 'class': 'form-control bottom'})


class LoginForm(forms.ModelForm):
    username_or_mobile = forms.CharField(max_length=150)
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username_or_mobile', 'password',)
        # field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username_or_mobile'].widget = forms.TextInput(attrs={'placeholder': 'username/mobile', 'class': 'form-control top'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'form-control middle'})
