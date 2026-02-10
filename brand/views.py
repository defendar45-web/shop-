
from django.db import models
from django.shortcuts import render
from brand.models import Brands


def brands(request):
    return render(request, 'brand/brands.html', {
        'brands': Brands.objects.all()
    })
