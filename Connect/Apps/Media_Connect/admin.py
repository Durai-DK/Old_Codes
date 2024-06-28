from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


admin.site.register(Assign_Job)
admin.site.register(Rating)


class DomainAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Domain, DomainAdmin)


class ResourceAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Resource, ResourceAdmin)