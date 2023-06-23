from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import IndividualClient

@receiver(pre_save, sender=IndividualClient)
def set_reg_number(sender, instance, **kwargs):
    if not instance.reg_number:  # Проверяем, не было ли уже установлено значение reg_number
        instance.reg_number = str(instance.pk)  # Используем значение ID в качестве reg_number