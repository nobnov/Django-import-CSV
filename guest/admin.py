from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from import_export.formats import base_formats

from guest.models import Guest


# Register your models here.
class GuestResource(resources.ModelResource):
    class Meta:
        model = Guest
        fields = ('id', 'name', 'job', 'age')
        import_id_fields = ['id']


class GuestAdmin(ImportExportActionModelAdmin):
    list_display = (
        'name',
        'job',
        'age'
    )

    resource_class = GuestResource
    formats = [base_formats.CSV]


admin.site.register(Guest, GuestAdmin)
