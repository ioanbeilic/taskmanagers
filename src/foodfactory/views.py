from django.shortcuts import render

from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext_lazy


def home(request):
    trans = translate(language="es")
    return render(request, "index.html", {"trans": trans})


def translate(language):
    current_lang = get_language()
    try:
        activate(language)
        text = gettext_lazy("hello")
    finally:
        activate(current_lang)
    return text
