from django.contrib import admin
from .models import CropManagement, Field,Area,Vegetable,GrowingCrop,Reminder

# Register your models here.
admin.site.register(Field)
admin.site.register(Area)
admin.site.register(Vegetable)
admin.site.register(GrowingCrop)
admin.site.register(CropManagement)
admin.site.register(Reminder)

#admin.site.register(CustomUser)
