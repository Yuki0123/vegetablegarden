from django.contrib import admin
from .models import CropManagement, Field,Area,Vegetable,GrowingCrop

# Register your models here.
admin.site.register(Field)
admin.site.register(Area)
admin.site.register(Vegetable)
admin.site.register(GrowingCrop)
admin.site.register(CropManagement)
