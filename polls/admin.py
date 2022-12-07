from django.contrib import admin

from .models import Question, Choice


# The lines of codes bellow is to change the position of the functions in the admin page on the website


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# The class above is to make the layout more organized putting everything beside each other

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # This line bellow adds a “Filter” sidebar that allows people to filter the list of changes by the pub_date field
    list_filter = ['pub_date']
    # The line bellow adds a search box at the top of the change list
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
