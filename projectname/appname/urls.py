from django.urls import path
from .views import RecordAPIView
urlpatterns = [
        path('route/', RecordAPIView.as_view(), name='user-login'),
]