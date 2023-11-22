from django.urls import path

from postsapp.views import PostsListView,PostDetailView

urlpatterns = [
    path('list/', PostsListView.as_view()),
    path('list/<int:pk>/', PostDetailView.as_view()),
]