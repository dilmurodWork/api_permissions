from rest_framework import generics, permissions

from .models import PostModel
from .serializers import PostsSerializer
from .permissions import IsAuthorOrReadOnly


class PostsListView(generics.ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthorOrReadOnly,]
