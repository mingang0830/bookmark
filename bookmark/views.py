from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
# Create your views here.
