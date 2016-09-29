from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Zocbo
from .forms import ZocboForm


def index(request):
    return render(request, "blog/index.html", {})


@login_required
def zocbo_list(request):
    zocbo_list = Zocbo.objects.all()
    return render(request, "blog/zocbo_list.html", {
        "zocbo_list": zocbo_list,
        })


@login_required
def zocbo_detail(request, pk):
    zocbo = get_object_or_404(Zocbo, pk=pk)
    return render(request, "blog/zocbo_detail.html", {
        "zocbo": zocbo,
        })


@login_required
def zocbo_new(request):
    if request.method == "POST":
        form = ZocboForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect("blog:zocbo_detail", form.pk)
    else:
        form = ZocboForm()
    return render(request, "forms.html", {
        "form": form,
        })


@login_required
def zocbo_edit(request, pk):
    zocbo = get_object_or_404(Zocbo, pk=pk)
    if request.method == "POST" and request.user == zocbo.author:
        form = ZocboForm(request.POST, request.FILES, instance=zocbo)
        if form.is_valid():
            form.save()
            return redirect("blog:zocbo_detail", zocbo.pk)
    else:
        form = ZocboForm(instance=zocbo)
    return render(request, "forms.html",{
        "form":form,
        })













