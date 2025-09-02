from django.contrib import admin
from .models import AboutUs
from django_summernote.admin import SummernoteModelAdmin

@admin.register(AboutUs)
class AboutUsAdmin(SummernoteModelAdmin):
    list_display = ('title', 'updated_on')
    summernote_fields = ('content',)

# Register your models here.
