from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView

from trackings.models import Tracking


class IndexView(ListView):
    model = Tracking
