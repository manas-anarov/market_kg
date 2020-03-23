from django.shortcuts import render


from rest_framework.generics import (CreateAPIView)
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from un_shop.models import OrderItem

from .serializers import (
	addSerializer,
	)

from .forms import (
	PostForm,
	)


from django.urls import reverse_lazy


class CreateOrder(CreateAPIView):
	serializer_class = addSerializer
	queryset = OrderItem.objects.all()


class CreateViewFront(SuccessMessageMixin, CreateView):
	model = OrderItem
	template_name = "create.html"
	success_url = "un-shop/create-front/"
	# fields = ['telephone', 'first_name', 'last_name', 'address']
	success_message = "Заказ Принят"
	form_class = PostForm

	success_url = reverse_lazy('api-un-shop:web-create')
	# fields = [
	# 		'telephone',
	# 		'whatsapp',
	# 		'first_name',
	# 		'last_name',
	# 		'address',
	# 		# 'passport_foto',
	# 	]

	# def get_success_url(self):
	# 	return reverse('api-un-shop:web-create')
