from rest_framework.viewsets import ModelViewSet
from blog.models import Blog
from .serializers import BlogSerializer


# Create your views here.

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
