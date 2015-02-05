from django.shortcuts import render
from django.http import HttpResponse

from groupings import get_groups

from groupings.models import SubmitForm

import itertools

# Create your views here.

def main_page(request):
    context = {}

    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            pretty_print = ''
            count = 0
            result = form.groups()
            for rounds in result:
                #if len(round) < len(result[0]):
                #    break
                count += 1
                pretty_print = pretty_print + "Round: " + str(count) + "\r"
                for group in rounds:
                    pretty_print = pretty_print + str(group) + "\r"
                pretty_print = pretty_print + "\r\r"
            context = {
                'form' : SubmitForm,
                'result' : pretty_print,
            }
        else:
            return HttpResponse('what have you done')
    else:
        context = {
            'form' : SubmitForm,
        }         
    return render(request, 'groupings/page.html', context)

    
