# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.urls import path
from . import views

app_name = 'vegetablegarden'

urlpatterns = [
   path('', views.GrowingCropList.as_view(), name = 'growingcrop_list'),
   path('growingcrop_create/',views.GrowingCropCreate.as_view(), name='growingcrop_create'),
   path('growingcrop/<int:pk>/update/',views.GrowingCropUpdate.as_view(), name='growingcrop_update'),
   path('growingcrop/<int:pk>/delete/',views.GrowingCropDelete.as_view(), name='growingcrop_delete'),
   path('cropmanagement_list/<int:growingcrop_pk>/',views.CropManagementList.as_view(), name='cropmanagement_list'),
   path('cropmanagement_create/<int:growingcrop_pk>/',views.CropManagementCreate.as_view(), name='cropmanagement_create'),
   path('cropmanagement_update/<int:pk>/',views.CropManagementUpdate.as_view(), name='cropmanagement_update'),
   path('cropmanagement_delete/<int:pk>/',views.CropManagementDelete.as_view(), name='cropmanagement_delete'),
   path('vegetable_create/',views.VegetableCreate.as_view(), name='vegetable_create'),
   path('reminder_create/<int:cropmanagement_pk>/',views.ReminderCreate.as_view(), name='reminder_create'),
]

