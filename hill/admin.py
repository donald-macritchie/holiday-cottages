from django.contrib import admin
from .models import Cottage, CottageImages, Amenities, ThingsToKnow, Booking, ContactMessage, ThingsToDo
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Cottage)
class CottageAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('content')


admin.site.register(CottageImages)
admin.site.register(Amenities)
admin.site.register(ThingsToKnow)
admin.site.register(Booking)
admin.site.register(ContactMessage)
admin.site.register(ThingsToDo)
