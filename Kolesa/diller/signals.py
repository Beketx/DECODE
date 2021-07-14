import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from diller.models import Favourites
from . import models
logger = logging.getLogger(__name__)

@receiver(post_save, sender=models.Publications)
def developer_created(sender, instance, created, **kwargs):
    if created:
        logger.debug('Publication created')

@receiver(post_delete, sender=models.Publications)
def del_user(sender, instance,deleted, **kwargs):
    if deleted:
        logger.debug('Publication deleted')