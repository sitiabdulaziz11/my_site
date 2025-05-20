from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    """ Comment form
    """
    class Meta:
        """ meta class to configur comment model with form
        """
        model = Comment
        # fields = "__all__"  # here we don't add all fiels b/c post field in comments model not set by user. so we use execlude, to list execluded field like below
        exclude = ["post"]
        labels =  {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment"
        } # to overwrit labels of field in comment model.
