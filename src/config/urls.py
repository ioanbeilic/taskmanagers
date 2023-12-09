from django.contrib import admin
from django.urls import path, include

from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    path(_("admin/"), admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
    path("food-factory/", include("foodfactory.urls", namespace="food factory")),
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
)
