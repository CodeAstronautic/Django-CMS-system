from django.urls import path,include
from . import views
from django.contrib.auth import views as v

urlpatterns=[
    path('dashboard/',views.index_page,name='man_index'),
    path('assign_project/',views.assigned_project,name='assigned_project'),
    path('view_detail/<int:pk>',views.view_details,name='man_details'),
    path('gallery/<int:pk>',views.gallery,name='man-gallery'),
    path('material/<int:pk>',views.material_details,name='material_man'),
    path('material_request/<int:pk>',views.material_request,name='material_request'),
    path('material_request_status/<int:pk>',views.material_request_status,name='material_request_status'),
    path('add_material_man/<int:pk>/<int:id>',views.add_material_man,name='add_material_man'),
    path('project_enquiry/<int:pk>',views.project_enquiry,name='project_enquiry'),
    path('daily_report',views.daily_report,name='daily_report'),
    path('my_report/',views.my_report,name='my_report'),

    path('manager-password-change/',v.PasswordChangeView.as_view(template_name='manager1/password_change.html'),name='change_password_manager'),
    path('manager-password-change-done/',v.PasswordChangeView.as_view(template_name='manager1/password_change_done.html'),name='change_password_manager_done'),

    path('edit_manager_profile/',views.edit_manager_profile,name='edit_manager_profile'),
    path('profile_pic/',views.profile_pic,name='profile_pic')
    

    


    
]
