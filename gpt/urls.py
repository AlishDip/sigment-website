from django.urls import path
from .views import GPTView

urlpatterns = [
    path('', GPTView.as_view(), name='gpt'),
]
