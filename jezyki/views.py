from django.shortcuts import render
from django.views.generic import TemplateView
from django.apps import apps
from .forms import LanguageForm
from .models import Article, Language
from django.core import serializers
from django.http import JsonResponse

# GET

def get_articles(request):
    if request.method == "GET":
        unfiltered = Article.objects.all()
        data = serializers.serialize("json", unfiltered, use_natural_foreign_keys=True)
        return JsonResponse(data, safe=False)

def article_list(request):
    form = LanguageForm(request.GET or None)  
    articles = []
    selected_language = None

    if form.is_valid():
        selected_language = form.cleaned_data['language']
        articles = Article.objects.filter(language=selected_language)

    return render(request, 'jezyki/article_list.html', {
        'form': form,
        'articles': articles,
        'selected_language': selected_language,
    })
#


class ArticleView(TemplateView):
    # strona główna artykułów -
    # zamienić nazwę na Wasz template
    template_name = "index.html"

