from django.contrib import admin
from django.db import models
from django import forms
from .models import Exercise, Comment
from .forms import ExerciseAdminForm

# Register your models here.
class ExerciseAdmin(admin.ModelAdmin):
    # dodac fieldset
    fields = ["title", "instruction", "assert_output", "language",]
    form = ExerciseAdminForm

class CommentAdmin(admin.ModelAdmin):
    # dodac fieldset
    fields = ["user", "exercise", "comment"]
    formfield_overrides = {
        models.CharField: {
            "widget": forms.Textarea(attrs={'rows': 3, 'cols': 60}) 
        }
    }


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Comment, CommentAdmin)
