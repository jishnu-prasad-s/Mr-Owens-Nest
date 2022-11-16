from .models import User
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['date_joined', 'is_active', 'last_login', 'groups', 'user_permissions']