from django.shortcuts import render
from .form import EmpForm


def index(request):
    if request.method == "POST":
        form = EmpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                pass
    else:
        form = EmpForm()
    return render(request, 'index.html', {'form': form})