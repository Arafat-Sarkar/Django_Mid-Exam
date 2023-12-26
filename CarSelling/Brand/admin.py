
from django.contrib import admin
from .import models
from .models import brandmodel
class BrandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('Brand_Name',)}
    list_display = ['Brand_Name','slug']

admin.site.register(brandmodel,BrandsAdmin)

