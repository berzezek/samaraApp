from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html

from .models import Poll, Question, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'add_question')

    def add_question(self, obj):
        url = reverse('admin:polls_question_add') + "?poll=" + str(obj.id)
        return format_html(f'<a href="{url}">Добавить вопрос</a>')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['poll', 'title', 'add_choice']

    def add_choice(self, obj):
        url = reverse('admin:polls_choice_add') + "?question=" + str(obj.id)
        return format_html(f'<a href="{url}">Добавить варинат ответа</a>')

    def response_add(self, request, obj, post_url_continue=None):
        if "_addanother" in request.POST:
            return HttpResponseRedirect(reverse('admin:polls_question_add') + "?poll=" + str(obj.poll.id))
        return super().response_add(request, obj, post_url_continue)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_text', 'is_true']

    def response_add(self, request, obj, post_url_continue=None):
        print(request.POST)
        if "_addanother" in request.POST:
            return HttpResponseRedirect(reverse('admin:polls_choice_add') + "?question=" + str(obj.question.id))
        return super().response_add(request, obj, post_url_continue)


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
