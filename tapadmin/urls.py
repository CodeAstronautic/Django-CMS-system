from django.urls import path,include
from . import views
from django.contrib.auth import views as v
urlpatterns=[
    path('',views.index_page,name='index'),
    path('register',views.register_user,name='register'),
    path('login/',views.login_user,name='login_user'),

    path('logout',views.logout_user,name='logout_user'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('quote/',views.quotes,name='quote'),
    path('service_single/',views.service_single,name='service_single'),
    path('vaastu/',views.vaastu,name='vaastu'),
    path('booking_flat/',views.booking_flat,name='booking_flat'),
    path('blog_details/',views.blog_detail,name='blog_detail'),
    path('contact/',views.contact,name='contact'),
    path('project_full_width/',views.project_full_width,name='project_full_width'),
    path('projects/',views.project_view,name='user_project'),
    path('project_three_column/',views.project_three_column,name='project_three_column'),
    path('project_single/<int:pk>',views.project_single,name='project_single'),
    path('home-01/',views.home_01,name='home_01'),
    path('home-02/',views.home_02,name='home_02'),
    path('project_grid_two_column/',views.project_grid_two_column,name='project_grid_two_column'),
    path('gallery/',views.gallery,name='gallery'),


    path('password-change/',v.PasswordChangeView.as_view(template_name='customer/password_change.html'),name='change_password'),
    path('password-change-done/',v.PasswordChangeView.as_view(template_name='customer/password_change_done.html'),name='password_change_done'),
    path('password-reset/',v.PasswordResetView.as_view(template_name='customer/password_reset.html',email_template_name='customer/password_reset_email.html',subject_template_name='customer/password_reset_email_subject.txt'),name='password_reset'),
    path('password-reset-done/',v.PasswordResetView.as_view(template_name='customer/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',v.PasswordResetConfirmView.as_view(template_name='customer/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',v.PasswordResetCompleteView.as_view(template_name='customer/password_reset_complete.html'),name='password_reset_complete'),
    
    path('Commercial/',views.Commercial_project,name='Commercial'),
    path('Residential/',views.Residential_project,name='Residential'),
    path('enqiry_submit/<int:id>',views.enqiry_submit,name='enqiry_submit')
    

]
