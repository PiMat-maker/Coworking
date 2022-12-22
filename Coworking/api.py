from ninja import Router
from django.shortcuts import render

router = Router()


@router.get('/')
def main_page(request):
    return render(request, 'main.html')


@router.get('/request')
def create_request(request):
    return render(request, 'request.html', context={
        'answer': ''
    })


@router.get('/rate')
def rate(request):
    return render(request, 'rate.html', context={
        'answer': ''
    })
