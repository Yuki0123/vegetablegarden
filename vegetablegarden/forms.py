from django.utils import timezone
from django import forms
from django.db.models import fields
from .models import Area,GrowingCrop,Vegetable,CropManagement

class GrowingCropCreateForm(forms.ModelForm):
    
    class Meta:
        model = GrowingCrop
        exclude = ('user',)
        widgets = {
            'vegatable' : forms.Select(attrs={'class': 'input'}),
            'variety': forms.TextInput(attrs={'class': 'input'}),
            'area': forms.Select(attrs={'class': 'input'}),
            'seeding_date': forms.SelectDateWidget(attrs={'class': 'input'}),
            'planting_date': forms.SelectDateWidget(attrs={'class': 'input'}),
            'transplanting_date': forms.SelectDateWidget(attrs={'class': 'input'}),
            'harvest_date_start': forms.SelectDateWidget(attrs={'class': 'input'}),
            'harvest_date_end': forms.SelectDateWidget(attrs={'class': 'input'})
            }

    def __init__(self, *args, **kwargs):
        self.area=kwargs.pop('area_pk',None)

        super(GrowingCropCreateForm, self).__init__(*args, **kwargs)
        self.fields['area'].initial = self.area

class GrowingCropUpdateForm(forms.ModelForm):

    class Meta:
        model=GrowingCrop
        exclude = ('user',)
        widgets = {
            'vegatable' : forms.Select(attrs={'class': 'input'}),
            'variety': forms.TextInput(attrs={'class': 'input'}),
            'area': forms.Select(attrs={'class': 'input'}),
            'seeding_date': forms.SelectDateWidget(attrs={'class': 'input'}),
            'planting_date': forms.SelectDateWidget(attrs={'class': 'input'}),
            'transplanting_date': forms.SelectDateWidget(attrs={'class': 'input'}),
            'harvest_date_start': forms.SelectDateWidget(attrs={'class': 'input'}),
            'harvest_date_end': forms.SelectDateWidget(attrs={'class': 'input'})
            }
class CropManagementCreateForm(forms.ModelForm):

    class Meta:
        model=CropManagement
        exclude=('user',)
        widgets = {
            'growing_crop' : forms.Select(attrs={'class': 'input'}),
            'title': forms.TextInput(attrs={'class': 'input'}),
            'text': forms.Textarea(attrs={'class': 'textarea'}),
            'date': forms.SelectDateWidget(attrs={'class': 'dropdown'})
            }
        

    def __init__(self, *args, **kwargs):
        self.growingcrop_pk = kwargs.pop('growingcrop_pk')

        super(CropManagementCreateForm, self).__init__(*args, **kwargs)
        
        self.fields['growing_crop'].initial = self.growingcrop_pk

        self.fields['growing_crop'].widget = forms.HiddenInput()
        self.fields['growing_crop'].label = ''

        self.fields['date'].initial = timezone.now().date()

class CropManagementUpdateForm(forms.ModelForm):

    class Meta:
        model=CropManagement
        exclude=('user','growing_crop')
        widgets = {
            'growing_crop' : forms.Select(attrs={'class': 'input'}),
            'title': forms.TextInput(attrs={'class': 'input'}),
            'text': forms.Textarea(attrs={'class': 'textarea'}),
            'date': forms.SelectDateWidget(attrs={'class': 'dropdown'})
            }

        

class AreaCreateForm(forms.ModelForm):

    class Meta:
        model=Area
        exclude = ('user', )

class VegetableCreateForm(forms.ModelForm):

    class Meta:
        model=Vegetable
        exclude = ('user',)
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'input'}),
            'icon': forms.TextInput(attrs={'class': 'input'}),
            }
