from django.contrib.postgres.fields import ArrayField
from django.db import models

from vision_web_test import constants


optional = {'null': True, 'blank': True}


class SharedAttributesMixin(models.Model):
    container_bg_color = models.CharField(max_length=20, **optional)
    content_bg_color_major = models.CharField(max_length=20, **optional)
    content_bg_color_minor = models.CharField(max_length=20, **optional)
    title_font_size = models.CharField(max_length=20, **optional)
    title_font_color = models.CharField(max_length=20, **optional)
    text_font_size = models.CharField(max_length=20, **optional)
    text_font_color_major = models.CharField(max_length=20, **optional)
    text_font_color_minor = models.CharField(max_length=20, **optional)
    button_bg_color = models.CharField(max_length=20, **optional)
    button_font_size = models.CharField(max_length=20, **optional)
    button_font_color = models.CharField(max_length=20, **optional)

    def get_template_name(self):
        return constants.ELEMENTS_TEMPLATES[self.__class__.__name__]

    class Meta:
        abstract = True


class BlockWithImageAndList(SharedAttributesMixin):
    title = models.CharField(max_length=100, **optional)
    images = models.FileField(upload_to="images", **optional)
    list_items = ArrayField(models.CharField(max_length=100), **optional, size=5)

    def __str__(self):
        return f'{self.id} / BlockWithImageAndList'

    class Meta:
        db_table = "block_image_and_list"


class BlockWithFourTexts(SharedAttributesMixin):
    top_left_text = models.CharField(max_length=255, **optional)
    top_right_text = models.CharField(max_length=255, **optional)
    bottom_left_text = models.CharField(max_length=255, **optional)
    bottom_right_text = models.CharField(max_length=255, **optional)

    def __str__(self):
        return f'{self.id} / BlockWithFourTexts'

    class Meta:
        db_table = "block_four_text"


class BlockWithTitleTextAndButton(SharedAttributesMixin):
    title = models.CharField(max_length=100, **optional)
    text = models.TextField(**optional)
    button_text = models.CharField(max_length=30, **optional)
    button_action = models.CharField(max_length=30, **optional)

    def __str__(self):
        return f'{self.id} / BlockWithTitleTextAndButton'

    class Meta:
        db_table = "block_title_text_and_button"


class BlockWithTitleTextImageAndButtons(SharedAttributesMixin):
    images = models.FileField(upload_to="images", **optional)
    title = models.CharField(max_length=100, **optional)
    text = models.TextField(**optional)
    first_button_text = models.CharField(max_length=30, **optional)
    first_button_action = models.CharField(max_length=30, **optional)
    second_button_text = models.CharField(max_length=30, **optional)
    second_button_action = models.CharField(max_length=30, **optional)

    def __str__(self):
        return f'{self.id} / BlockWithTitleTextImageAndButtons'

    class Meta:
        db_table = "block_title_text_image_and_buttons"
