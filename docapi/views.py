from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Users
from .models import Test
from .serializers import UsersSerializers
from .testserializers import TestSerializers


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


@csrf_exempt
def test_list(request):
    if request.method == 'GET':
        test = Test.objects.all()
        testSerializer = TestSerializers(test, many=True)
        return JsonResponse(testSerializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        testSerializer = TestSerializers(data=data)

    if testSerializer.is_valid():
        testSerializer.save()
        return JsonResponse(testSerializer.data, status=201)
    return JsonResponse(testSerializer.errors, status=404)
