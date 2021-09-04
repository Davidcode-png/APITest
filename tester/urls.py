from django.urls import path
from .views import CommentReactionView



urlpatterns = [
    path('react/',CommentReactionView.as_view(),name='react')
]
