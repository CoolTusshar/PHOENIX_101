from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Feedback,Question_List
from .choices import INSTITUTION_CHOICES,USER_CHOICES

# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
#
#
# class PostForm(forms.ModelForm):
#     class Meta:
#         content = forms.CharField(widget=PagedownWidget)
#         model = Post
#         fields = [
#             "title",
#             "brief",
#             "content",
#         ]
#
# class ProfileForm(forms.ModelForm):
#     gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect )
#     bio = forms.CharField(max_length=140)
#     profilePic = forms.ImageField()
#
#     class Meta:
#         model = Profile
#         fields = [
#             "gender",
#             "bio",
#             "profilePic",
#         ]

class Feedback_Form_1(forms.ModelForm):
    user_type = forms.ChoiceField(choices=USER_CHOICES, widget=forms.RadioSelect)
    user_id = forms.IntegerField(required=True)
    answer_0 = forms.IntegerField()
    answer_1 = forms.IntegerField()
    answer_2 = forms.IntegerField()
    answer_3 = forms.IntegerField()
    answer_4 = forms.IntegerField()
    answer_5 = forms.IntegerField()
    answer_6 = forms.IntegerField()
    answer_7 = forms.IntegerField()
    answer_8 = forms.IntegerField()
    answer_9 = forms.IntegerField()

    class Meta:
        model = Feedback
        fields = [
            'user_type',
            'user_id',
            'answer_0',
            'answer_1',
            'answer_2',
            'answer_3',
            'answer_4',
            'answer_5',
            'answer_6',
            'answer_7',
            'answer_8',
            'answer_9'
                  ]
