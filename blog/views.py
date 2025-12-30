from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer,GameInputSerializer
import random


class ItemsView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class Game(APIView):
    def get(self,request):
        a = ["you died","you won","you got a gift"]
        random_item = random.choice(a)
        return Response(random_item)
    def post(self, request):
        # داده‌ها را با serializer اعتبارسنجی می‌کنیم
        serializer = GameInputSerializer(data=request.data)
        if serializer.is_valid():
            ggg = serializer.validated_data['choice']
            if ggg == 1:
                return Response({"me ssage": "go to room"})
            else:
                return Response({"message": "invalid choice"})
        else:
            return Response(serializer.errors, status=400)
        
class humanViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer