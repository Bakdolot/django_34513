from django.contrib import admin

from .models import Question, Choice, Some, SomeM2M


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["choice", "choice_set", "somem2m", "SomeM2M_question+", "somem2m_set", "__module__", "__doc__", "objects"]
    

class ChoiceAdmin(admin.ModelAdmin):
    pass
    

class SomeAdmin(admin.ModelAdmin):
    pass
    
    
class SomeM2MAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Some, SomeAdmin)
admin.site.register(SomeM2M, SomeM2MAdmin)