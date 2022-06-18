from django.shortcuts import render
from .models import Vegetable, GrowingCrop,CropManagement
from django.views import generic
from django.urls import reverse_lazy,reverse
from django.shortcuts import get_list_or_404, redirect
from .forms import GrowingCropCreateForm, GrowingCropUpdateForm,CropManagementCreateForm,CropManagementUpdateForm,AreaCreateForm,VegetableCreateForm

# Create your views here.
class VegetableCreate(generic.FormView):
    form_class= VegetableCreateForm
    template_name="growingcrop_create.html"
    model = Vegetable        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='野菜を追加'
        return context

    def form_valid(self, form):
        instance=form.save(commit=False)
        instance.user=self.request.user
        self.object=form.save()
        return redirect('vegetablegarden:growingcrop_list')

class GrowingCropList(generic.ListView):
    model = GrowingCrop
    template_name="growingcrop_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='ただいま栽培中'

        context['cropmanagements']=CropManagement.objects.order_by('-date')[:5]
        context['harvestedcrop']=GrowingCrop.objects.filter(harvest_date_end__isnull=False).order_by('area__name')
        return context

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user.pk,harvest_date_end__isnull=True).order_by('area__name')

class GrowingCropCreate(generic.FormView):
    form_class= GrowingCropCreateForm
    template_name="growingcrop_create.html"
    model = GrowingCrop        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='栽培情報を追加'
        return context

    def form_valid(self, form):
        instance=form.save(commit=False)
        instance.user=self.request.user
        self.object=form.save()
        return redirect('vegetablegarden:growingcrop_list')

class GrowingCropUpdate(generic.UpdateView):
    form_class= GrowingCropUpdateForm
    template_name = 'growingcrop_update.html'
    model = GrowingCrop

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='栽培情報を編集'

        return context

    def form_valid(self, form):
        instance=form.save(commit=False)
        instance.user=self.request.user
        self.object=form.save()
        
        return redirect('vegetablegarden:growingcrop_list')

class GrowingCropDelete(generic.DeleteView):
    model=GrowingCrop
    template_name="growingcrop_delete.html"
    success_url=reverse_lazy('vegetablegarden:growingcrop_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='栽培している野菜の削除'
        return context

class CropManagementList(generic.ListView):
    template_name="cropmanagement_list.html"
    model = CropManagement
    all_data=CropManagement.objects.all()
    growingcrop=GrowingCrop.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        queryset=super().get_queryset().filter(user=self.request.user.pk,growing_crop=self.kwargs['growingcrop_pk']).order_by('-date','-pk')
        if len(queryset)==0:
            context['count']=0

        context['growingcrop']=self.growingcrop.filter(pk=self.kwargs['growingcrop_pk'])
        context['title']='お世話ノート'

        return context

    def get_queryset(self):
        queryset=super().get_queryset().filter(user=self.request.user.pk,growing_crop=self.kwargs['growingcrop_pk']).order_by('-date','-pk')
        
        if len(queryset) == 0:
            queryset=self.all_data

        return queryset

class CropManagementCreate(generic.FormView):
    form_class= CropManagementCreateForm
    template_name="cropmanagement_create.html"
    model = CropManagement        
    growingcrop=GrowingCrop.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['growingcrop']=self.growingcrop.filter(pk=self.kwargs['growingcrop_pk'])
        context['title']='お世話記録を追加'
        return context

    def get_form_kwargs(self):
        kwargs = super(CropManagementCreate, self).get_form_kwargs()
        kwargs['growingcrop_pk'] = self.kwargs['growingcrop_pk']
        return kwargs    

    def form_valid(self, form):
        instance=form.save(commit=False)
        instance.user=self.request.user
        self.object=form.save()
        return redirect('vegetablegarden:cropmanagement_list', growingcrop_pk=self.kwargs['growingcrop_pk'])

class CropManagementUpdate(generic.UpdateView):
    form_class= CropManagementUpdateForm
    template_name = 'cropmanagement_update.html'
    model = CropManagement

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='お世話記録を編集'
        return context

    def form_valid(self, form):
        instance=form.save(commit=False)
        #instance.management_group=get_object_or_404(ManagementGroup,pk=self.kwargs['mg_pk'])
        instance.user=self.request.user
        self.object=form.save()
        
        print(self.object.growing_crop.pk)

        return redirect('vegetablegarden:cropmanagement_list', growingcrop_pk=self.object.growing_crop.pk)


class CropManagementDelete(generic.DeleteView):
    model=CropManagement
    template_name="cropmanagement_delete.html"
    #success_url=reverse_lazy('vegetablegarden:growingcrop_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='お世話記録の削除'
        return context

    def get_success_url(self):
        print(self.object.growing_crop.pk)
        return reverse('vegetablegarden:cropmanagement_list', kwargs={"growingcrop_pk":self.object.growing_crop.pk})

