from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Collection, Link
User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class Usercollection(forms.Form):
    collection = forms.ModelChoiceField(queryset=Collection.objects.all(),
    widget=forms.Select(attrs={"hx-get": "load_links/", "hx-target": "#id_link"}))

    link = forms.ModelChoiceField(queryset=Link.objects.none())


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "collection" in self.data:
            collection_id = int(self.data.get("collection"))
            self.fields["link"].queryset = Link.objects.filter(collection_id=collection_id)