from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
# Create your views here.
from .models import KirrURL


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})



class KirrCBView(View):
    def get(self, request,shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

