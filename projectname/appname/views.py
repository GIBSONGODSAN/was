from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Records
from .serializers import RecordSerializer

class RecordAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = RecordSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'Record created'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'status': 'Record not created'}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def get(self, request):
        try:
            param = request.query_params.get('value1')
            record = Records.objects.get(value1=param)
            serializer = RecordSerializer(record)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Records.DoesNotExist:
            return Response({'status': 'Record not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request):
        data = request.data
        value1 = data.get('value1')
        record = Records.objects.get(value1=value1)
        serializer = RecordSerializer(record, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Record updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        data = request.data
        value1 = data.get('value1')
        record = Records.objects.get(value1=value1)
        record.delete()
        return Response({'status': 'Record deleted'}, status=status.HTTP_200_OK)