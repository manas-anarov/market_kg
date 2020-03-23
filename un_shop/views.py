from django.shortcuts import render


from rest_framework.generics import (CreateAPIView)
from django.views.generic.edit import CreateView

from un_shop.models import OrderItem

from .serializers import (
	addSerializer,
	)


class CreateOrder(CreateAPIView):
	serializer_class = addSerializer
	queryset = OrderItem.objects.all()


class CreateViewFront(CreateView):
	model = OrderItem
	template_name = "create.html"
	fields = ['telephone', 'first_name', 'last_name', 'address']
