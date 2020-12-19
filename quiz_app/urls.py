from django.urls import path
from .views import index,register, user_login, user_logout, QuizList, question, google_login, leaderBoard
urlpatterns = [
    path('',index, name='landing_page'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='signuppage'),
    path('question/<int:id>/', question, name='question'),
    path('google/', google_login, name='google'),
    path('leaderboard/', leaderBoard, name='leaderboard')
]
