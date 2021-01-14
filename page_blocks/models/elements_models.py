from django.contrib.postgres.fields import ArrayField
from django.db import models

from vision_web_test import constants


optional = {'null': True, 'blank': True}


class BlockWithImageAndList(models.Model):
    images = models.ImageField(upload_to="images", **optional)
    list_items = ArrayField(models.CharField(max_length=50), **optional, size=5)

    def __str__(self):
        return f'{self.id} / BlockWithImageAndList'

    def get_template_name(self):
        return constants.ELEMENTS_TEMPLATES[self.__class__.__name__]

    class Meta:
        db_table = "block_image_and_list"


class BlockWithFourTexts(models.Model):
    top_left_text = models.CharField(max_length=255, **optional)
    top_right_text = models.CharField(max_length=255, **optional)
    bottom_left_text = models.CharField(max_length=255, **optional)
    bottom_right_text = models.CharField(max_length=255, **optional)

    def __str__(self):
        return f'{self.id} / BlockWithFourTexts'

    def get_template_name(self):
        return constants.ELEMENTS_TEMPLATES[self.__class__.__name__]

    class Meta:
        db_table = "block_four_text"


class BlockWithTitleTextAndButton(models.Model):
    title = models.CharField(max_length=100, **optional)
    text = models.TextField(**optional)
    button_text = models.CharField(max_length=30, **optional)
    button_action = models.CharField(max_length=30, **optional)

    def __str__(self):
        return f'{self.id} / BlockWithTitleTextAndButton'

    def get_template_name(self):
        return constants.ELEMENTS_TEMPLATES[self.__class__.__name__]

    class Meta:
        db_table = "block_title_text_and_button"


class BlockWithTitleTextImageAndButtons(models.Model):
    images = models.ImageField(upload_to="images", **optional)
    title = models.CharField(max_length=100, **optional)
    text = models.TextField(**optional)
    first_button_text = models.CharField(max_length=30, **optional)
    first_button_action = models.CharField(max_length=30, **optional)
    second_button_text = models.CharField(max_length=30, **optional)
    second_button_action = models.CharField(max_length=30, **optional)

    def __str__(self):
        return f'{self.id} / BlockWithTitleTextImageAndButtons'

    def get_template_name(self):
        return constants.ELEMENTS_TEMPLATES[self.__class__.__name__]

    class Meta:
        db_table = "block_title_text_image_and_buttons"
