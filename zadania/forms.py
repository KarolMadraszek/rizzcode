from django import forms
from .models import Solution

class SolutionUploadForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['code_file']

class SQLSolutionForm(forms.Form):
    solution_text = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':80}))

    from django import forms
from .models import Exercise

class ExerciseAdminForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'
        widgets = {
            'title': forms.Textarea(attrs={'rows': 1, 'cols': 80}),
            'instruction': forms.Textarea(attrs={'rows': 6, 'cols': 80}),
            'assert_output': forms.Textarea(attrs={'rows': 1, 'cols': 80}),
        }

