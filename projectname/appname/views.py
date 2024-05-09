from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Records

class RecordAPIView(APIView):
    def post(self, request):
        data = request.data
        value1 = data.get('value1')
        value2 = data.get('value2')
        value3 = data.get('value3')
        value4 = data.get('value4')
        record = Records(value1=value1, value2=value2, value3=value3, value4=value4)
        record.save()
        return Response({'status': 'Record created'}, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        records = Records.objects.all()
        data = []
        for record in records:
            data.append({
                'value1': record.value1,
                'value2': record.value2,
                'value3': record.value3,
                'value4': record.value4
            })
        return Response(data, status=status.HTTP_200_OK)
    
    def put(self, request):
        data = request.data
        value1 = data.get('value1')
        value2 = data.get('value2')
        value3 = data.get('value3')
        value4 = data.get('value4')
        record = Records.objects.get(value1=value1)
        record.value2 = value2
        record.value3 = value3
        record.value4 = value4
        record.save()
        return Response({'status': 'Record updated'}, status=status.HTTP_200_OK)
    
    def delete(self, request):
        data = request.data
        value1 = data.get('value1')
        record = Records.objects.get(value1=value1)
        record.delete()
        return Response({'status': 'Record deleted'}, status=status.HTTP_200_OK)