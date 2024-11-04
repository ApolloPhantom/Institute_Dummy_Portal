from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Faculty, Alumni
from .forms import FacultyForm, AlumniForm
from .utils import search_faculty, search_alumni
from django.conf import settings
import os

def home(request):
    return render(request, 'home.html')

# Faculty views
def faculty_list(request):
    faculty = Faculty.objects.all()
    return render(request, 'faculty/list.html', {'faculty': faculty})

def faculty_detail(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    return render(request, 'faculty/detail.html', {'faculty': faculty})

@login_required
def faculty_create(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST, request.FILES)
        if form.is_valid():
            faculty = form.save()
            return redirect('faculty_list')
    else:
        form = FacultyForm()
    return render(request, 'faculty/form.html', {'form': form})

@login_required
def faculty_edit(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        form = FacultyForm(request.POST, request.FILES, instance=faculty)
        if form.is_valid():
            faculty = form.save()
            return redirect('faculty_detail', pk=faculty.pk)
    else:
        form = FacultyForm(instance=faculty)
    return render(request, 'faculty/form.html', {'form': form, 'faculty': faculty})

@login_required
def faculty_delete(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        if faculty.image:
            if os.path.isfile(faculty.image.path):
                os.remove(faculty.image.path)
        faculty.delete()
        print("Successfully deleted")
        return redirect('faculty_list')
    return render(request, 'faculty/confirm_delete.html', {'faculty': faculty})

def faculty_search(request):
    query = request.GET.get('q', '')
    faculty = search_faculty(query) if query else Faculty.objects.all()
    return render(request, 'faculty/faculty_grid.html', {'faculty': faculty})

# Alumni views
def alumni_list(request):
    alumni = Alumni.objects.all()
    return render(request, 'alumni/list.html', {'alumni': alumni})

def alumni_detail(request, pk):
    alumni = get_object_or_404(Alumni, pk=pk)
    return render(request, 'alumni/detail.html', {'alumni': alumni})

@login_required
def alumni_create(request):
    if request.method == 'POST':
        form = AlumniForm(request.POST, request.FILES)
        if form.is_valid():
            alumni = form.save()
            return redirect('alumni_list')
    else:
        form = AlumniForm()
    return render(request, 'alumni/form.html', {'form': form})

@login_required
def alumni_edit(request, pk):
    alumni = get_object_or_404(Alumni, pk=pk)
    if request.method == 'POST':
        form = AlumniForm(request.POST, request.FILES, instance=alumni)
        if form.is_valid():
            alumni = form.save()
            return redirect('alumni_detail', pk=alumni.pk)
    else:
        form = AlumniForm(instance=alumni)
    return render(request, 'alumni/form.html', {'form': form, 'alumni': alumni})

@login_required
def alumni_delete(request, pk):
    alumni = get_object_or_404(Alumni, pk=pk)
    if request.method == 'POST':
        if alumni.image:
            if os.path.isfile(alumni.image.path):
                os.remove(alumni.image.path)
        alumni.delete()
        return redirect('alumni_list')
    return render(request, 'alumni/confirm_delete.html', {'alumni': alumni})

def alumni_search(request):
    query = request.GET.get('q', '')
    alumni = search_alumni(query) if query else Alumni.objects.all()
    return render(request, 'alumni/alumni_grid.html', {'alumni': alumni})