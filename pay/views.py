from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from pay.models import Paidusers, ContactData
from pay.serializators import ContactSerialization, PaidusersSerialization

from time import sleep

class home(TemplateView):
    template_name = 'pay/home.html'

class payment(CreateAPIView):
    model = Paidusers
    queryset = Paidusers.objects.all()
    http_method_names = ['post']
    serializer_class = PaidusersSerialization

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # place of payment
            return Response(200)
        else:
            return Response(serializer.data)

class contacts(APIView):
    model = ContactData
    queryset = ContactData.objects.all()
    serializer_class = ContactSerialization

    def get(self, request):
        return Response(self.serializer_class(self.queryset.all(), many=True).data)