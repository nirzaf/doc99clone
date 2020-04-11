from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Users
from .serializers import UsersSerializers


# Create your views here.
@csrf_exempt
def users_list(request):
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializers(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializers(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=404)
