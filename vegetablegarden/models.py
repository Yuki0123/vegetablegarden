from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.conf import settings

# Create your models here.
class Field(models.Model):
    name = CharField(verbose_name='畑', max_length=255)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Area(models.Model):
    name = CharField(verbose_name='栽培エリア', max_length=255)
    field = ForeignKey(Field, verbose_name='畑', on_delete = models.CASCADE)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Vegetable(models.Model):
    name = CharField(verbose_name='野菜', max_length=255)
    icon = CharField(verbose_name='Icon', max_length=255, default='<i class="fa-solid fa-seedling"></i>', null=True, blank=True)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class GrowingCrop(models.Model):
    vegetable = ForeignKey(Vegetable,verbose_name='野菜', null=True, on_delete = models.SET_NULL)
    variety = CharField(verbose_name='品種', max_length=255, null=True,  blank=True)
    area = ForeignKey(Area, verbose_name='栽培エリア', null=True, on_delete = models.SET_NULL)
    seeding_date = DateField(verbose_name='種まき日', null=True, blank=True)
    planting_date = DateField(verbose_name='植付日', null=True, blank=True)
    transplanting_date = DateField(verbose_name='移植日', null=True, blank=True)
    harvest_date_start =  DateField(verbose_name='収穫開始日', null=True, blank=True)
    harvest_date_end =  DateField(verbose_name='収穫完了日', null=True, blank=True)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return '{} {}'.format(self.vegetable,self.variety)

class CropManagement(models.Model):
    growing_crop = ForeignKey(GrowingCrop, verbose_name='作物',null=True, on_delete=models.SET_NULL)
    title = CharField(verbose_name='項目', max_length=255)
    text=TextField(verbose_name='内容', null=True, blank=True)
    date = DateField(verbose_name='実施日', null=True, blank=True)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

