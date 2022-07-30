from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.conf import settings
from django.core.validators import FileExtensionValidator

# Create your models here.
class Field(models.Model):
    name = models.CharField(verbose_name='畑', max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Area(models.Model):
    name = models.CharField(verbose_name='栽培エリア', max_length=255)
    field = models.ForeignKey(Field, verbose_name='畑', on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Vegetable(models.Model):
    name = models.CharField(verbose_name='野菜', max_length=255)
    icon = models.CharField(verbose_name='Icon', max_length=255, default='<i class="fa-solid fa-seedling"></i>', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class GrowingCrop(models.Model):
    vegetable = models.ForeignKey(Vegetable,verbose_name='野菜', null=True, on_delete = models.SET_NULL)
    variety = models.CharField(verbose_name='品種', max_length=255, null=True,  blank=True)
    area = models.ForeignKey(Area, verbose_name='栽培エリア', null=True, on_delete = models.SET_NULL)
    seeding_date = models.DateField(verbose_name='種まき日', null=True, blank=True)
    planting_date = models.DateField(verbose_name='植付日', null=True, blank=True)
    transplanting_date = models.DateField(verbose_name='移植日', null=True, blank=True)
    harvest_date_start =  models.DateField(verbose_name='収穫開始日', null=True, blank=True)
    harvest_date_end =  models.DateField(verbose_name='収穫完了日', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return '{} {}'.format(self.vegetable,self.variety)

class CropManagement(models.Model):
    growing_crop = models.ForeignKey(GrowingCrop, verbose_name='作物',null=True, on_delete=models.SET_NULL)
    title = models.CharField(verbose_name='項目', max_length=255)
    text= models.TextField(verbose_name='内容', null=True, blank=True)
    image = models.ImageField(verbose_name='画像', upload_to='vegetablegarden/', null=True, blank=True)
    date = models.DateField(verbose_name='実施日', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title

class Reminder(models.Model):
    cropmanagement = models.ForeignKey(CropManagement, verbose_name='栽培管理',null=True, on_delete=models.SET_NULL)
    title = models.CharField(verbose_name='項目', max_length=255)
    days = models.IntegerField(verbose_name='日数', null=True, blank=True)
    unit = models.CharField(verbose_name='単位', max_length=255)
    base_date = models.DateField(verbose_name='基準日', null=True, blank=True)
    calculation_date = models.DateField(verbose_name='算出日', null=True, blank=True)
    text= models.TextField(verbose_name='内容', null=True, blank=True)

    def __str__(self) -> str:
        return '{} {}'.format(self.title,self.calculation_date)
