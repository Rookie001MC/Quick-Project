from django.contrib import admin
from joke_truy_na.models import Prisoner
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PrisonerAdmin(SummernoteModelAdmin):
    list_display = ('prisoner_name', 'prisoner_id', 'prisoner_jail_section','prisoner_jail_room')
    search_fields = ['prisoner_name', 'prisoner_id']
    summernote_fields = (
        'prisoner_current_charges',
        'prisoner_about',
        'prisoner_old_charges',
    )
    pass

admin.site.register(Prisoner, PrisonerAdmin)