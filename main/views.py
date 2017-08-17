from django.shortcuts import render,redirect
from .forms import Feedback_Form_1,SignUpForm,f_form_0
from .models import Feedback
from .questions import ANONYMUS_QUESTIONS,FACULTY_QUESTIONS,STUDENT_QUESTIONS
from django.contrib.auth import login, authenticate
import json

# Create your views here.
def home(request):
    return render(request,'main/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


def feedback(request):
    if request.method == 'POST':
        form = Feedback_Form_1(request.POST or None)
        form_0 = f_form_0(request.POST or None)
        if form.is_valid():
            feedback_obj = Feedback()
            form.save()
            if request.user.is_authenticated():
                feedback_obj.user_type = request.user.user_type
                feedback_obj.user_name = request.user.user_name
            else:
                feedback_obj.user_name = form_0.cleaned_data.get('user_name')
            ans_list = [
                form.cleaned_data.get('answer_0'),
                form.cleaned_data.get('answer_1'),
                form.cleaned_data.get('answer_2'),
                form.cleaned_data.get('answer_3'),
                form.cleaned_data.get('answer_4'),
                form.cleaned_data.get('answer_5'),
                form.cleaned_data.get('answer_6'),
                form.cleaned_data.get('answer_7'),
                form.cleaned_data.get('answer_8'),
                form.cleaned_data.get('answer_9')
            ]
            feedback_obj.answer_list = json.dumps(ans_list)
            feedback_obj.save()
            return redirect('home')
    else:
        form = Feedback_Form_1(request.POST or None)
        form_0 = f_form_0(request.POST or None)
        if request.user.is_authenticated():
            if request.user.user_type == 1:
                context = {'form': form,'q_list':STUDENT_QUESTIONS}
            else:
                context = {'form': form, 'q_list':FACULTY_QUESTIONS}
        else:
            context = {'form': form,'form_0': form_0, 'q_list': ANONYMUS_QUESTIONS}
        return render(request,'main/feedback.html',context)



def map_school(request):
    return render(request, 'main/school_near.html')