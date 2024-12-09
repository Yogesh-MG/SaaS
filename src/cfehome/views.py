from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from visit.models import PageVisit

def home(request):
    queryset = PageVisit.objects.all()
    qr = PageVisit.objects.filter(no_visit=request.path)
    context = {
        'user_name': 'yogesh',
        'queryset': queryset,
        'qr':qr
    }
    PageVisit.objects.create(no_visit=request.path)
    return render(request, 'home.html',context)
