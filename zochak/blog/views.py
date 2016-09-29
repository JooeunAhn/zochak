from django.shortcuts import render, get_object_or_404
from .models import Zocbo


def index(request):
    return render(request, "blog/index.html", {})


def zocbo_list(request):
    zocbo_list = Zocbo.objects.all()
    return render(request, "blog/zocbo_list.html", {
        "zocbo_list": zocbo_list,
        })


def zocbo_detail(request, pk):
    zocbo = get_object_or_404(Zocbo, pk=pk)
    return render(request, "blog/zocbo_detail.html", {
        "zocbo": zocbo,
        })
