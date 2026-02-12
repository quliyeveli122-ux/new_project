from django.http import JsonResponse
from .serializer import CoffeeSerializer
from .models import Coffee


def get_all_coffees(request):
    coffees = Coffee.objects.all()
    serializer = CoffeeSerializer(coffees, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_iced_coffees(request):
    coffees = Coffee.objects.filter(category="Soyuq içkilər")
    serializer = CoffeeSerializer(coffees, many=True)
    return JsonResponse(serializer.data, safe=False)
