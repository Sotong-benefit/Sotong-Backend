from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
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
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': '이메일을 입력해주세요'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'비밀번호를 입력해주세요'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 각 필드에 class 추가
        self.fields['email'].widget.attrs['class'] = 'input-form'
        self.fields['password'].widget.attrs['class'] = 'input-form'