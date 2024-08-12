from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
from users.models import CustomUser

CustomUser = get_user_model()

from allauth.account.forms import LoginForm


class YourLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(YourLoginForm, self).__init__(*args, **kwargs)
        self.fields["password"].widget = forms.PasswordInput()

        # You don't want the `remember` field?
        if "remember" in self.fields.keys():
            del self.fields["remember"]

        helper = FormHelper()
        helper.form_show_labels = False
        helper.layout = Layout(
            Field("login", placeholder="Email address"),
            Field("password", placeholder="Password"),
            FormActions(
                Submit("submit", "Log me in to Cornell Forum", css_class="btn-primary")
            ),
        )
        self.helper = helper


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
