from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from .models import *
from heist.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from datetime import date, datetime, timedelta
from django.db.models import Q
from django.shortcuts import get_object_or_404

# Menu selection views

def home(request):
    return render(request, 'home.html')

def info(request):
    return render(request, 'info/info.html')