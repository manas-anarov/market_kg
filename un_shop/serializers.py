from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
)
from un_shop.models import OrderItem


class addSerializer(ModelSerializer):
	class Meta:
		model = OrderItem
		fields = [
			'telephone',
			'whatsapp',
			'first_name',
			'last_name',
			'address',
			# 'passport_foto',
		]

