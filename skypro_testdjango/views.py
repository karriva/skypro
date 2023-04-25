from django.http import JsonResponse, HttpResponse, Http404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from skypro_testdjango.models import Data
from skypro_testdjango.serializers import DataSerializer


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def data_list(request, pk=None):
    if pk:
        try:
            data_object = Data.objects.get(pk=pk)
            serializer = DataSerializer(data_object)
            return JsonResponse(serializer.data, safe=False)
        except Data.DoesNotExist:
            return HttpResponse(status=404)
    data_objects = Data.objects.all()
    serializer = DataSerializer(data_objects, many=True)
    return JsonResponse(serializer.data, safe=False)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PATCH'])
def modify(request, pk):
    data = Data.objects.get(pk=pk)
    if data.author != request.user:
        raise Http404("You are not allowed to edit this Post")
    ser_data = DataSerializer(instance=data, data=request.data, partial=True)

    if ser_data.is_valid():
        ser_data.save()
        return JsonResponse(ser_data.data)
    else:
        return Http404("You are not allowed to edit this Post")
