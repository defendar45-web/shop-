from django.shortcuts import render

from promotion.models import Promo


# Create your views here.
def promotion(request):
     return render(request, 'promotion/promo.html', {
          'promotion': Promo.objects.all()
     })