from django import forms

from .models import OrderItem

class PostForm(forms.ModelForm):

	telephone = forms.CharField(required=True, label='Телефон')
	whatsapp = forms.CharField(required=False, label='whatsapp')
	first_name = forms.CharField(required=True, label='Имя')
	last_name = forms.CharField(required=True, label='Фамилия')
	address = forms.CharField(required=True, label='Адрес')
	# url = forms.URLField(label='Your website', required=False)

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