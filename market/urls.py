from django.urls import path
from market.views.auth import AuthView

urlpatterns = [
    path('user_login/', AuthView.as_view())
]