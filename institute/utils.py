from django.db.models import Q
from .models import Faculty, Alumni

def search_faculty(query):
    return Faculty.objects.filter(
        Q(name__icontains=query) |
        Q(department__icontains=query) |
        Q(designation__icontains=query)
    )

def search_alumni(query):
    return Alumni.objects.filter(
        Q(name__icontains=query) |
        Q(degree__icontains=query) |
        Q(current_company__icontains=query)
    )