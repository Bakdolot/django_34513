from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["pub_date", "question_text", "choice"]
    

class ChoiceAdmin(admin.ModelAdmin):
    fields = ["question", "choice_text", "votes"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)