from rest_framework.viewsets import ModelViewSet
from .models import Lead
from .serializers import LeadSerializer
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class LeadAPIViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,DjangoFilterBackend]
    search_fields = ['first_name', 'last_name', 'email', 'age', 'hotel_name', 'hotel_address', 'phone_number', 'url', 'description', 'category__name', 'agent__first_name']
    ordering_fields = ['first_name', 'last_name', 'email', 'age', 'hotel_name', 'hotel_address', 'phone_number', 'url', 'description', 'category__name', 'agent__first_name']
    filterset_fields = ['first_name', 'last_name', 'email', 'age', 'hotel_name', 'hotel_address', 'phone_number', 'url', 'description', 'category__name', 'agent__first_name']

    def list(self, request, *args, **kwargs):
        """
            Return a list of all Leads from database.
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
            Create a Lead on database.
        """
        phone_number = request.data.get('phone_number')
        if phone_number:
            leads = Lead.objects.filter(phone_number=phone_number)
            if leads:
                lead = leads[0]
                serializer = LeadSerializer(lead)
                return Response(serializer.data, status=status.HTTP_200_OK)

        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
            Return a Lead from database.
        """
        return super().retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
            Applies partial update to a Lead.
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
            Delete a Lead from database.
        """
        return super().destroy(request, *args, **kwargs)
