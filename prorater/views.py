from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, NewProjectForm, UpdateProfileForm, ReviewForm
from django.contrib import messages
from .models import Project, Review
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile
from .serializer import ProfileSerializer, ProjectsSerializer
from wwwrate import serializer

# Create your views here.

def index(request):

    projects = Project.objects.all()
    if request.method == 'POST':
        upload_form = NewProjectForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.instance.owner = request.user.profile
            upload_form.save()

            return redirect('index')

    else:
        upload_form = NewProjectForm()



    context = {'upload_form': upload_form, 'projects':projects}
    return render(request, 'index.html', context)

