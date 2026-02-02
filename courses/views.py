from django.shortcuts import render, get_object_or_404

from courses.models import Seminars


# Create your views here.
def seminars(request):
    return render(request, 'courses/base.html',{
        "seminars":Seminars.objects.all(),
    }
         )

def seminar_detail(request, id):
    seminar = get_object_or_404(Seminars, id=id)
    return render(request, 'courses/seminar_detail.html', {
        'seminar': seminar
    })