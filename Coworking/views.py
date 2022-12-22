from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.views.decorators.http import require_POST
from . import models

from Coworking.models import Coworking, OccupiedSpaceInfo


class CreateRequest(forms.Form):
    coworking_name = forms.ChoiceField(
        choices=(('Kronverkskii 2-nd floor', 'Kronverkskii 2-nd floor'),
                 ('Kronverkskii 3-rd floor', 'Kronverkskii 3-rd floor'),
                 ('Lomonosova 2-nd floor', 'Lomonosova 2-nd floor'),
                 ('Lomonosova 4-th floor', 'Lomonosova 4-th floor'),
                 ),
    )


# Create your views here.
def create_request(request):
    f = CreateRequest(request.GET)

    if f.is_valid():
        coworking_name = f.data.get('coworking_name')
        coworking = Coworking.objects.get(name=coworking_name)
        last_occupied_info = OccupiedSpaceInfo.objects.filter(coworking=coworking).order_by('-time')[0]
        free_place_number = coworking.places_number - last_occupied_info.places_occupied
        return render(request, 'request.html', context={
            'answer': f'Number of free places at {coworking_name}: {free_place_number}'
        })

    return HttpResponse(f'No Hello world')


class Rate(forms.Form):
    CHOICES = (('Kronverkskii 2-nd floor', 'Kronverkskii 2-nd floor'),
               ('Kronverkskii 3-rd floor', 'Kronverkskii 3-rd floor'),
               ('Lomonosova 2-nd floor', 'Lomonosova 2-nd floor'),
               ('Lomonosova 4-th floor', 'Lomonosova 4-th floor'),
               )
    coworking_name = forms.ChoiceField(choices=CHOICES)
    mark = forms.IntegerField(min_value=0, max_value=10)


@require_POST
def rate(request):
    f = Rate(request.POST)

    if f.is_valid():
        coworking_name = f.cleaned_data['coworking_name'].lower()
        mark = f.cleaned_data['mark']
        coworking = Coworking.objects.get(name=coworking_name)
        rate = models.Rate(coworking=coworking, mark=mark)
        rate.save()
        return render(request, 'rate.html', context={
            'answer': 'Thanks for your mark'
        })

    return HttpResponse('Blabla')
