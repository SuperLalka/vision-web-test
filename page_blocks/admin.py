from django import forms
from django.apps import apps
from django.contrib import admin

from page_blocks.models import (
    Block,
    BlockWithImageAndList,
    BlockWithFourTexts,
    BlockWithTitleTextAndButton,
    BlockWithTitleTextImageAndButtons,
)
from vision_web_test import constants


class ElementTypeForm(forms.ModelForm):
    element_type = forms.ChoiceField(label="Тип элемента",
                                     choices=constants.ELEMENTS_TEMPLATES_CHOICES)

    def save(self, *args, **kwargs):
        super(ElementTypeForm, self).save(*args, **kwargs)
        element_model_name = self.cleaned_data.pop('element_type')

        element_model = apps.get_model('page_blocks', element_model_name)
        element = element_model.objects.create()
        block = Block.objects.create(**self.cleaned_data,
                                     content_object=element)
        return block


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('tag', 'sorting', 'is_active')
    list_filter = ('is_active',)
    search_fields = ['name']
    form = ElementTypeForm


# Elements models

admin.site.register(BlockWithImageAndList)
admin.site.register(BlockWithFourTexts)
admin.site.register(BlockWithTitleTextAndButton)
admin.site.register(BlockWithTitleTextImageAndButtons)
