""" life invader views """

""" django """
from django.http import HttpResponse    
from django.http import JsonResponse

""" utilities """
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=str(now)
    ))

def sort_integers(request):
    """import pdb; pdb.set_trace()"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sort_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sort_ints,
        'message': 'Integers sorted succesfully.'
    }
    return HttpResponse(
        JsonResponse(data), 
        content_type='application/json'
    )

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry, {} you are not allowed here'.format(name)
    else:
        message = 'Hello!, {} welcome to lifeInvader'.format(name)
    return HttpResponse(message)
