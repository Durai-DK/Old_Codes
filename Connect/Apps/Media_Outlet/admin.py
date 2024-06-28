from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

admin.site.register(Status)
admin.site.register(Floor_Diagram)
admin.site.register(full_img)


class ShowroomAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Showroom,ShowroomAdmin)


class RSMAdmin(ImportExportModelAdmin):
    pass


admin.site.register(RSM, RSMAdmin)


class ASMAdmin(ImportExportModelAdmin):
    pass


admin.site.register(ASM, ASMAdmin)


class ManagerAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Manager, ManagerAdmin)


class RegionAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Region, RegionAdmin)


class StateAdmin(ImportExportModelAdmin):
    pass


admin.site.register(State, StateAdmin)


class Showroom_DetailsAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Showroom_Details, Showroom_DetailsAdmin)


class class_DetailsAdmin(ImportExportModelAdmin):
    pass


admin.site.register(class_Details, class_DetailsAdmin)


class BrandAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Brand, BrandAdmin)


class Brand_typeAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Brand_type, Brand_typeAdmin)


class Brand_LocationAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Brand_Location, Brand_LocationAdmin)


class Material_TypeAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Material_Type, Material_TypeAdmin)


class Light_TypeAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Light_Type, Light_TypeAdmin)


class AssetAdmin(ImportExportModelAdmin):
    pass


admin.site.register(AssetManagement,AssetAdmin)


class VendorsAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Vendors,VendorsAdmin)


class Ad_StatusAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Ad_Status,Ad_StatusAdmin)