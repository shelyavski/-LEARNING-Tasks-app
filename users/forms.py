from django.forms import ModelForm
from .models import User, Profile


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'profile_image']

    def __int__(self, *args, **kwargs):
        super(ProfileEditForm).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})  # TODO: Check why forms don't display properly
