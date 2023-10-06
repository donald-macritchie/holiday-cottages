from django.contrib import admin
from .models import Cottage, CottageImages, Amenities
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Cottage)
class CottageAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('content')


admin.site.register(CottageImages)
admin.site.register(Amenities)

