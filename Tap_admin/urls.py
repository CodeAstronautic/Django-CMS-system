from django.urls import path
from .views import *
from django.contrib.auth import views 
from django.contrib.auth import views as v

urlpatterns=[
    path('home',index_page,name='index_admin'),
    path('',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('new_proj',new_proj,name='new_proj'),
    path('ongoing/',ongoing,name='ongoing'),
    path('details/<int:pk>',detail_project,name='details'),
    path('delete_project/<int:pk>',delete_project,name='delete_project'),
    path('add_manager/',add_manager,name='add_manager'),
    path('gallery/<int:pk>',gallery,name='gallery'),
    path('management/<int:pk>',management,name='manage'),
    path('manage_profile',manage_profile,name='manage_profile'),
    #path('edit_profile',edit_profile,name='edit_profile'),
    path('delete/<int:pk>',delete_image,name='delete_image'),
    path('dashboard/',index_page),
    path('password_change/',views.PasswordChangeView.as_view(template_name='password_change.html'),name='change_password'),
    path('password_change_done/',views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='change_password_done'),
    path('material/<int:pk>',material_view,name='material_view'),
    path('add_material/<int:pk>',add_material,name='add_material'),
    path('add_material_type/<int:pk>',add_material_type,name='add_material_type'),
    path('delete_mat_type/<int:pk>/<int:id>',delete_mat_type,name='delete_mat_type'),
    path('sale/<int:pk>',sale,name='sale'),
    path('update_sale/<int:pk>',update_sale,name='update_sale'),
    
    path('project_enquiry/<int:pk>',project_enquiry,name='admin_project_enquiry'),
    path('new_enquiry/',new_enquiry,name='new_enquiry'),
    path('manage_manager',manage_manager,name='manage_manager'),
    path('delete_manager/<int:pk>',delete_manager,name='delete_manager'),
    path('manager_reporting/',manager_reporting,name='manager_reporting'),
    path('edit_profile_admin/',edit_profile_admin,name='edit_admin'),
    path('admin-password-change/',v.PasswordChangeView.as_view(template_name='Tap_admin/password_change.html'),name='change_password_admin'),
    path('admin-password-change-done/',v.PasswordChangeView.as_view(template_name='Tap_admin/password_change_done.html'),name='change_password_admin_done'),
    

    
    
   
]