from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.validators import EmailValidator
from django.contrib.auth.forms import SetPasswordForm

class SignUpForm(UserCreationForm):
    username = forms.EmailField(validators=[EmailValidator(message='이메일 형식이 아닙니다.')])
    first_name = forms.CharField(max_length=10, required=True)
    #email = forms.EmailField(label='', required=True, widget=forms.EmailInput(attrs={'class': 'input-form', 'placeholder': '이메일을 입력해주세요'}))
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'first_name', 'password1', 'password2']

        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 각 필드에 placeholder를 추가합니다.
        self.fields['username'].widget.attrs['placeholder'] = '이메일을 입력해주세요'
        self.fields['first_name'].widget.attrs['placeholder'] = '이름을 입력해주세요'
        self.fields['password1'].widget.attrs['placeholder'] = '비밀번호를 입력해주세요'
        self.fields['password2'].widget.attrs['placeholder'] = '비밀번호를 확인해주세요'

        # 각 필드에 class 추가
        self.fields['username'].widget.attrs['class'] = 'input-form'
        self.fields['first_name'].widget.attrs['class'] = 'input-form'
        self.fields['password1'].widget.attrs['class'] = 'input-form'
        self.fields['password2'].widget.attrs['class'] = 'input-form'

        # 각 필드의 label과 help_text를 비우기
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = None
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = None

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': '이메일을 입력해주세요'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'비밀번호를 입력해주세요'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 각 필드에 class 추가
        self.fields['username'].widget.attrs['class'] = 'input-form'
        self.fields['password'].widget.attrs['class'] = 'input-form'


class RecoveryPwForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput,)

    class Meta:
        fields = ['username']

    def __init__(self, *args, **kwargs):
        super(RecoveryPwForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = '아이디'
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_id',
        })

class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label = '새 비밀번호'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['new_password2'].label = '새 비밀번호 확인'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })