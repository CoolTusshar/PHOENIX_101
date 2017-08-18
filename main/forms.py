from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Feedback,Profile
from .choices import USER_CHOICES,RADIO_CHOICES,SCHOOL_CHOICES

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )


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
class ProfileForm(forms.ModelForm):
    school = forms.ChoiceField(choices=SCHOOL_CHOICES, widget=forms.RadioSelect)
    user_type = forms.ChoiceField(choices=USER_CHOICES,widget=forms.RadioSelect)

    class Meta:
        model = Profile
        fields = [
            "school",
            "user_type",
        ]

class Feedback_Form_1(forms.ModelForm):
    answer_0 = forms.ChoiceField(choices=RADIO_CHOICES, widget= forms.RadioSelect)
    answer_1 = forms.ChoiceField(choices=RADIO_CHOICES, widget= forms.RadioSelect)
    answer_2 = forms.ChoiceField(choices=RADIO_CHOICES, widget= forms.RadioSelect)
    answer_3 = forms.ChoiceField(choices=RADIO_CHOICES, widget= forms.RadioSelect)
    answer_4 = forms.ChoiceField(choices=RADIO_CHOICES, widget= forms.RadioSelect)
    answer_5 = forms.ChoiceField(choices=RADIO_CHOICES, widget= forms.RadioSelect)
    answer_6 = forms.ChoiceField(choices=RADIO_CHOICES, widget= forms.RadioSelect)
    answer_7 = forms.ChoiceField(choices=RADIO_CHOICES, widget= forms.RadioSelect)
    answer_8 = forms.ChoiceField(choices=RADIO_CHOICES, widget= forms.RadioSelect)
    answer_9 = forms.ChoiceField(choices=RADIO_CHOICES, widget= forms.RadioSelect)

    class Meta:
        model = Feedback
        fields = [
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
class f_form_0(forms.ModelForm):
    user_name = forms.CharField(max_length=10)
    class Meta:
        model = Feedback
        fields = [ 'user_name']