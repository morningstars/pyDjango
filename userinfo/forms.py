from django import forms


class RegForm(forms.Form):
    username = forms.CharField(label='请输入姓名', initial="无名氏", required=False)
    password = forms.CharField(label='请输入密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='重复输入密码', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 6:
            raise forms.ValidationError('用户名太短')
        return username

    def clean_password(self):
        pwd = self.cleaned_data['password']
        # 验证
        return pwd

    def clean(self):
        pwd1 = self.cleaned_data['password']
        pwd2 = self.cleaned_data['password2']
        if pwd1 != pwd2:
            raise forms.ValidationError('两次密码不一致')
        return self.cleaned_data
