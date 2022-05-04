from django.contrib import admin
from django.urls import path
from api.views import get_grammars

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grammars/', get_grammars)
]
