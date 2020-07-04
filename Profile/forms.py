from django.contrib.auth.forms import UserCreationForm
from .models import ShopUser

class ShopUserCreationForm(UserCreationForm):

    class Meta:
        model = ShopUser
        fields = ('first_name', 'last_name', 'username', 'email', 'instagram_handle')