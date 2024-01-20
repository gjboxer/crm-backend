from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CategoryAPIViewSet(ModelViewSet):
    """
        API endpoint that allows Categories to be viewed or edited.
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        """
            Return a list of all Categories from database.
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
            Create a Category on database.
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
            Return a Category from database.
        """
        return super().retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
            Applies partial update to a Category.
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
            Delete a Category from database.
        """
        return super().destroy(request, *args, **kwargs)
