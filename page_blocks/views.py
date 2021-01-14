from django.shortcuts import render

from page_blocks.models import (
    Block
)


def index(request):
    return render(request, 'index.html', context={
        'blocks': Block.objects.filter(is_active=True).order_by('sorting')
    })
