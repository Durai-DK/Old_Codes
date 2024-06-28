from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class Assign_ToAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Assign_To, Assign_ToAdmin)


class Assign_ByAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Assign_By, Assign_ByAdmin)


class Job_ForAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Job_For, Job_ForAdmin)


class Job_TypeAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Job_Type, Job_TypeAdmin)


class Design_TypeAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Design_Type, Design_TypeAdmin)


class Job_FormAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Job_Form, Job_FormAdmin)