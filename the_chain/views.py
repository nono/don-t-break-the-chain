from django.shortcuts import render_to_response, get_object_or_404
from dont_break_the_chain.the_chain.models import Calendar, Check


def index(request):
    cals = Calendar.objects.all()
    return render_to_response('calendars/index.html', {'calendars': cals})

def show(request, calendar_id):
    cal = get_object_or_404(Calendar, pk=calendar_id)
    return render_to_response('calendars/show.html', {'calendar': cal})
