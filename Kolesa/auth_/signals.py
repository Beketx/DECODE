import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from diller.models import Favourites
from . import models
logger = logging.getLogger(__name__)

# @receiver(post_save, sender=models.User)
# def developer_created(sender, instance, created, **kwargs):
#     if created:
#
#         models.Profile.objects.create(
#             user=instance,
#             first_name='Ashr',
#             last_name='Ashe',
#             phone_number='1231231231',
#             age=19,
#             gender='M'
#         )

@receiver(post_delete, sender=models.User)
def del_user(sender, instance,deleted, **kwargs):
    if deleted:
        logger.debug('User deleted')
