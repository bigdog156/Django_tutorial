from django.contrib import admin

# Register your models here.

from .models import Question, Choice, QuestionAdmin

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)