import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.views.generic import View, TemplateView, ListView
from app.models import Player
from app.serializers import PlayerSerializer
from rest_framework import generics


class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PlayerListView(ListView):
    model = Player
    template = "playerlist.html"

class PlayerListAPIView(View):
    def get(self, request):
        data = list(Player.objects.all().values())
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type="application/json")

class PlayerListAPIView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
