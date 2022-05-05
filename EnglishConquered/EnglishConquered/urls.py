from django.contrib import admin
from django.urls import path
from api.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('modules/', ModuleView.as_view()),
    path('modules/<str:id>/', ModuleDetailView.as_view()),
    path('grammar/', GrammarView.as_view()),
    path('grammar/<str:id>/', GrammarDetailView.as_view()),
]
