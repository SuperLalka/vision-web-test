from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


BLOCKS_NAME = "Enter a name for the block"
BLOCKS_SORTING = "Sequence of block pins on a page"


class Block(models.Model):
    name = models.CharField(max_length=100, help_text=BLOCKS_NAME)
    sorting = models.PositiveSmallIntegerField(default=None, help_text=BLOCKS_SORTING)
    is_active = models.BooleanField(default=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name
