from django.contrib import admin
from .models import Question, Quiz, Response, Payment
# Register your models here.



admin.site.register(Quiz)
admin.site.register(Question)
#admin.site.register(Scores)
admin.site.register(Response)
admin.site.register(Payment)