from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Response, Payment
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.core.paginator import Paginator
import json
import operator
import razorpay
# Create your views here.

client = razorpay.Client(auth=("rzp_test_uCzWnrEymDyUU5","yyeXf6bd5iCt2zciiRhBAGB3"))


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
    response = Response.objects.filter(quiz=quiz)
    leaderboard = Response.objects.filter(quiz=quiz)
    payment = Payment.objects.filter(quiz=quiz)
    leader_dict = {}
    for users in leaderboard:
        #print(users,users.scores)
        
        leader_dict[str(users)] = str(users.scores)

    sorted_dict = dict( sorted(leader_dict.items(),
                           key=lambda item: item[1],
                           reverse=True))

    # for key, value in isPaid.items():
    #     print(key,value)

    users_taken = []
    #print(payment)
    for username in response:
        users_taken.append(str(username))

    user_paid = []

    for userpaid in payment:
        user_paid.append(str(userpaid.user))
    print(user_paid)

    if str(request.user) in user_paid:
        if str(request.user) in users_taken:
            return render(request, 'question.html', {'quiz':quiz,'question_list': page_obj, 'isTaken': response, 'leader':sorted_dict})
        else:
            return render(request, 'question.html', {'quiz':quiz,'question_list': question})
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            amount = quiz.quiz_price

            client = razorpay.Client(
                auth=("rzp_test_uCzWnrEymDyUU5","yyeXf6bd5iCt2zciiRhBAGB3"
            ))

            payment = client.order.create({
                'amount': amount, 'currency': 'INR',
                'payment_capture': '1'
            })
            print('post request initiated for payment')
            if payment:
                new_payment = Payment(user=request.user, quiz=quiz, isPaid=True)
                new_payment.save()
                return render(request, 'question.html', {'quiz':quiz,'question_list': question})
        return render(request, 'order.html', {'quiz':quiz,'question_list': question})
    # if str(request.user) in users_taken:
    #     return render(request, 'question.html', {'quiz':quiz,'question_list': page_obj, 'isTaken': response, 'leader':sorted_dict})

    
    return render(request, 'order.html', {'quiz':quiz,'question_list': question})
    

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

def leaderBoard(request):
    return render(request, 'leaderboard.html', context={})


def answer(request,id):
    quiz = Quiz.objects.get(pk=id)
    print(quiz)
    if request.method == 'POST':
        print('post sdsdsd initiated')
        scores = request.POST.get('my_scores')
        print(scores)
        response = Response(user=request.user, quiz=quiz, scores=scores, isTaken=True)
        response.save()
        

def create_order(request):
    if request.method == 'POST':
        print('post request initiated')

    return render(request, 'order.html', {})
        
def success(request):
    return render(request, 'success.html')


def about(request):
    return render(request, 'about.html')

def faqs(request):
    return render(request, 'faqs.html')