from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList

# Create your views here.
def show_mywatchlist(request):
        data_watchlist = MyWatchList.objects.all()
        context = {
                'daftar_watchlist' : data_watchlist,
                'nama': 'Sania Rizqi Maharani',
                'student_id': '2006597001'
        }
        return render(request, "mywatchlist.html", context)

def show_xml_mywatchlist(request):
        data_xml = MyWatchList.objects.all()
        return HttpResponse(serializers.serialize("xml", data_xml), content_type="application/xml")

def show_json_mywatchlist(request):
        data_json = MyWatchList.objects.all()
        return HttpResponse(serializers.serialize("json", data_json), content_type="application/json")
