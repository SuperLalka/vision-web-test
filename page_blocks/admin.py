from django import forms
from django.apps import apps
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.postgres.fields import ArrayField
from django.forms import Textarea

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
        element_model_name = self.cleaned_data.pop('element_type')
        element_model = apps.get_model('page_blocks', element_model_name)

        if not self.instance:
            element = element_model.objects.create()
            block = Block.objects.create(**self.cleaned_data,
                                         content_object=element)
            return block
        return super(ElementTypeForm, self).save(*args, **kwargs)


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('tag', 'sorting', 'is_active')
    list_filter = ('is_active',)
    search_fields = ['name']
    form = ElementTypeForm


# Elements models

class BlockInline(GenericTabularInline):
    model = Block
    extra = 0


class BlockWithFourTextsAdmin(admin.ModelAdmin):
    inlines = [BlockInline]


class BlockWithImageAndListAdmin(admin.ModelAdmin):
    inlines = [BlockInline]
    formfield_overrides = {ArrayField: {
        'widget': Textarea(attrs={'rows': 3})
    }}


class BlockWithTitleTextAndButtonAdmin(admin.ModelAdmin):
    inlines = [BlockInline]


class BlockWithTitleTextImageAndButtonsAdmin(admin.ModelAdmin):
    inlines = [BlockInline]


admin.site.register(BlockWithFourTexts, BlockWithFourTextsAdmin)
admin.site.register(BlockWithImageAndList, BlockWithImageAndListAdmin)
admin.site.register(BlockWithTitleTextAndButton, BlockWithTitleTextAndButtonAdmin)
admin.site.register(BlockWithTitleTextImageAndButtons, BlockWithTitleTextImageAndButtonsAdmin)
