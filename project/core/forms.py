from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.auth.models import User
from models import Account



class UpdateProfileImage(forms.ModelForm):
    """
    Form for updating profile image
    """

    class Meta:
        model = Account
        fields = ['profile_image']

    profile_image = forms.ImageField()

    def clean_profile_image(self):
        profile_image = self.cleaned_data['profile_image']

        try:
            w, h = get_image_dimensions(profile_image)

            #validate dimensions
            max_height = 960
            max_width = 1280
            if w > max_width or h > max_height:
                raise forms.ValidationError(u'Please use an image that is {w} x {h} pixels or smaller.'.format(w=max_width, h=max_height))

            #validate content type
            main, sub = profile_image.content_type.split('/')
            if not (main == 'image' and sub in ['jpg', 'jpeg', 'pjpeg', 'png']):
                raise forms.ValidationError(u'Please use a JPEG or PNG image.')

            #validate file size
            if len(profile_image) > (2000 * 1024):
                raise forms.ValidationError('Profile image file size may not exceed 2MB.')

        except AttributeError:
            pass

        return profile_image
