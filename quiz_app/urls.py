from django.urls import path
from .views import index,register, user_login, user_logout, QuizList, question, google_login, leaderBoard, answer, create_order, success, about, faqs, contact, QuizListSearch
urlpatterns = [
    path('',QuizList.as_view(), name='landing_page'),
    path('search/', QuizListSearch.as_view(), name='quiz_search'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='signuppage'),
    path('quiz/<int:id>/', question, name='question'),
    path('google/', google_login, name='google'),
    path('leaderboard/', leaderBoard, name='leaderboard'),
    path('answer/<int:id>/', answer, name='answer'),
    path('create_order/', create_order, name='create_order'),
    path('success/', success, name='success'),
    path('about/', about, name='about'),
    path('faqs/', faqs, name='faqs'),
    path('contact/', contact, name='contact'),
]
