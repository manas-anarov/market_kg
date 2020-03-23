from django.db import models
from django.utils.translation import ugettext_lazy as _

class OrderItem(models.Model):
	timestamp = models.DateTimeField(auto_now=False, auto_now_add = True)
	first_name = models.CharField(max_length=400, blank=True,  verbose_name=_('Имя'))
	last_name = models.CharField(max_length=400, blank=True,  verbose_name=_('Фамилия'))
	telephone = models.CharField(max_length=400, blank=True, verbose_name=_('Телефон'))
	whatsapp = models.CharField(max_length=400, blank=True,  verbose_name=_('whatsapp'))
	
	address = models.CharField(max_length=400,  blank=True,  verbose_name=_('Адресс'))
	on_way = models.BooleanField(default=False,  verbose_name=_('Заказ обрабатывается'))
	ordered = models.BooleanField(default=False,  verbose_name=_('Заказ выполнен'))
	

	def __str__(self):
		return self.first_name