from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def upload(request):
    return render(request, 'mydata/upload.html')
