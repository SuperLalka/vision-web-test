from django.contrib.postgres.fields import ArrayField
from django.db import models

from vision_web_test import constants


class BlockWithImageAndList(models.Model):
    template_name = models.CharField(max_length=30, editable=False,
                                     default=constants.ELEMENTS_TEMPLATES[__qualname__])

    images = models.ImageField(upload_to="images")
    tags = ArrayField(models.CharField(max_length=50), blank=True, size=5)

    def __str__(self):
        return f'{self.id} / BlockWithImageAndList'


class BlockWithFourTexts(models.Model):
    template_name = models.CharField(max_length=30, editable=False,
                                     default=constants.ELEMENTS_TEMPLATES[__qualname__])

    top_left_text = models.CharField(max_length=255, null=True, blank=True)
    top_right_text = models.CharField(max_length=255, null=True, blank=True)
    bottom_left_text = models.CharField(max_length=255, null=True, blank=True)
    bottom_right_text = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.id} / BlockWithFourTexts'


class BlockWithTitleTextAndButton(models.Model):
    template_name = models.CharField(max_length=30, editable=False,
                                     default=constants.ELEMENTS_TEMPLATES[__qualname__])

    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField()
    button_text = models.CharField(max_length=30)
    button_action = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.id} / BlockWithTitleTextAndButton'


class BlockWithTitleTextImageAndButtons(models.Model):
    template_name = models.CharField(max_length=30, editable=False,
                                     default=constants.ELEMENTS_TEMPLATES[__qualname__])

    images = models.ImageField(upload_to="images")
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField()
    first_button_text = models.CharField(max_length=30)
    first_button_action = models.CharField(max_length=30, null=True, blank=True)
    second_button_text = models.CharField(max_length=30)
    second_button_action = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.id} / BlockWithTitleTextImageAndButtons'
