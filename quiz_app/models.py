from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Quiz(models.Model):
    quiz_author = models.CharField(max_length=50)
    quiz_name = models.CharField(max_length=256)
    quiz_description = models.CharField(max_length=500)
    quiz_price = models.FloatField(default=0)
    quiz_dead_line = models.DateTimeField()
    quiz_image = models.ImageField(upload_to='quiz_photo/',blank=True)
    quiz_slug = models.SlugField(blank=True)

    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)
    isTaken = models.BooleanField(default=False)
    points = models.IntegerField(default=30)
    def __str__(self):
        return self.question
        

class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    scores = models.IntegerField(default=0)
    isTaken = models.BooleanField(default=False)
    #time_taken = models.TimeField(blank=True)

    def __str__(self):
        return str(self.user)