from django.shortcuts import render
from .models import Quiz, Question, Response
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.core.paginator import Paginator
import json
# Create your views here.

def index(request):
    quiz = Quiz.objects.all()[::-1]
    context = {'quiz':quiz}
    return render(request, 'index.html', context=context)

    #print(quiz)

class QuizList(generic.ListView):
    model = Quiz
    context_object_name = 'quiz'
    template_name='index.html'
    

@login_required(login_url='/login/')
def question(request, id):
    quiz = Quiz.objects.get(pk=id)
    question = quiz.question_set.all()
    paginator_list = question
    paginator = Paginator(paginator_list, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
            # choice.votes+=1
            # choice.save()
            # print(choice.votes)
            # score = Scores(question=a, scores=100)
            # score.save()
            #print(page.question_text) 

    if request.method == 'POST':
        print('post ne initiated')
        scores = request.POST.get('my_scores')
        print(scores)
        return HttpResponse('Quiz Submitted Successfully')
    
    context = {'quiz':quiz,'question_list': question}

    return render(request, 'question.html', context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('landing_page'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('landing_page'))
            else:
                return HttpResponse('Acount Not Active')
        else:
            return render(request, 'login.html', context={'error':'Invalid Login Details, Try Again'})
    else:
        return render(request, 'login.html', context={})

def register(request):
    registered = False

    if request.method == 'POST':

        
        user_form = UserForm(data=request.POST)
        

        # Check to see both forms are valid
        if user_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()
            # Registration Successful!
            registered = True
            
        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'signup.html',
                          {'user_form':user_form,
                           'registered':registered})


def google_login(request):
    return render(request, 'google.html')

