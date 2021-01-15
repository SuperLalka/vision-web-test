from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from vision_web_test import constants


BLOCKS_NAME = "Enter a name for the block"
BLOCKS_SORTING = "Sequence of block pins on a page"

optional = {'null': True, 'blank': True}


class Block(models.Model):
    tag = models.SlugField()
    sorting = models.PositiveSmallIntegerField(default=0, help_text=BLOCKS_SORTING)
    is_active = models.BooleanField(default=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     related_name='content_type_block', editable=False,
                                     **optional)
    object_id = models.PositiveIntegerField(editable=False, **optional)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['is_active', '-sorting']


class User(AbstractUser):
    user_group = models.CharField(max_length=10, choices=constants.USER_GROUP,
                                  help_text='Select user group', default='Reader')

    def __str__(self):
        return self.username
