from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from lib.gpx import GpxParseError, parse_gpx
from lib.models import GpxData
from .forms import UploadGpxForm
from .models import RunningLog


@require_http_methods(['GET', 'POST'])
@login_required
def upload(request):
    if request.method == 'GET':
        return render(request, 'mydata/upload.html')

    else:
        # validates form fields
        form = UploadGpxForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'mydata/upload.html', dict(form=form))

        # creates GPX entry
        cd = form.cleaned_data
        try:
            gpx_data = GpxData(owner=request.user, description=cd['description'], has_timestamp=True)
            gpx_data.save()
        except:
            return render(request, 'mydata/upload.html', dict(form=form, has_db_error=True))

        # copies uploaded file
        try:
            with open(gpx_data.path, 'wb') as fout:
                for chunk in request.FILES['gpx'].chunks():
                    fout.write(chunk)
        except:
            gpx_data.delete()
            return render(request, 'mydata/upload.html', dict(form=form, has_io_error=True))

        # validates uploaded GPX file
        try:
            with open(gpx_data.path) as fin:
                gpx_records = parse_gpx(fin)
        except IOError:
            gpx_data.delete()
            return render(request, 'mydata/upload.html', dict(form=form, has_io_error=True))
        except GpxParseError:
            gpx_data.delete()
            return render(request, 'mydata/upload.html', dict(form=form, has_parse_error=True))

        if any(not r.has_timestamp for r in gpx_records):
            gpx_data.delete()
            return render(request, 'mydata/upload.html', dict(form=form, has_parse_error=True))

        # adds running log
        try:
            running_log = RunningLog(owner=request.user, description=cd['description'], gpx=gpx_data)
            running_log.save()
        except:
            gpx_data.delete()
            return render(request, 'mydata/upload.html', dict(form=form, has_db_error=True))

        #
        return render(request, 'mydata/upload.html', dict(has_no_error=True, running_log=running_log))
