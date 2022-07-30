from django.utils import timezone
from django import forms
from django.db.models import fields
from .models import Area,GrowingCrop, Reminder,Vegetable,CropManagement
from django.contrib.admin.widgets import AdminDateWidget

class GrowingCropCreateForm(forms.ModelForm):
    
    class Meta:
        model = GrowingCrop
        exclude = ('user',)
        widgets = {
            'vegatable': forms.Select(attrs={'class': 'uk-select'}),
            'variety': forms.TextInput(attrs={'class': 'uk-input'}),
            'area': forms.Select(attrs={'class': 'uk-select'}),
            'seeding_date' : AdminDateWidget(),
            'planting_date': AdminDateWidget(),
            'transplanting_date': AdminDateWidget(),
            'harvest_date_start': AdminDateWidget(),
            'harvest_date_end': AdminDateWidget(),
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
            'vegatable' : forms.Select(attrs={'class': 'uk-select'}),
            'variety': forms.TextInput(attrs={'class': 'uk-input'}),
            'area': forms.Select(attrs={'class': 'uk-select'}),
            'seeding_date': AdminDateWidget(),
            'planting_date': AdminDateWidget(),
            'transplanting_date': AdminDateWidget(),
            'harvest_date_start': AdminDateWidget(),
            'harvest_date_end': AdminDateWidget(),
            }
class CropManagementCreateForm(forms.ModelForm):

    class Meta:
        model=CropManagement
        exclude=('user',)
        widgets = {
            'growing_crop' : forms.Select(attrs={'class': 'uk-input'}),
            'title': forms.TextInput(attrs={'class': 'uk-input'}),
            'text': forms.Textarea(attrs={'class': 'uk-textarea'}),
            'date': AdminDateWidget(),
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
            'growing_crop' : forms.Select(attrs={'class': 'uk-input'}),
            'title': forms.TextInput(attrs={'class': 'uk-input'}),
            'text': forms.Textarea(attrs={'class': 'uk-textarea'}),
            'date': AdminDateWidget(),
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
            'name' : forms.TextInput(attrs={'class': 'uk-input'}),
            'icon': forms.TextInput(attrs={'class': 'uk-input'}),
            }

class ReminderCreateForm(forms.ModelForm):

    class Meta:
        model=Reminder
        exclude = ('user',)
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'uk-input'}),
            'days': forms.TextInput(attrs={'class': 'uk-input'}),
            'base_date': AdminDateWidget(),
            'calculation_date': AdminDateWidget(),
            'text': forms.Textarea(attrs={'class': 'uk-textarea'}),           
            }
    
    def __init__(self, *args, **kwargs):
        self.cropmanagement_pk = kwargs.pop('cropmanagement_pk')

        super(ReminderCreateForm, self).__init__(*args, **kwargs)
        
        self.fields['cropmanagement'].initial = self.cropmanagement_pk

        self.fields['cropmanagement'].widget = forms.HiddenInput()
        self.fields['cropmanagement'].label = ''

