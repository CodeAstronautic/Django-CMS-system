from django.contrib import admin

# Register your models here.
from manager. models import *
from django.contrib.auth import get_user_model
from . models import *
admin.site.register(ManagerProfile)
admin.site.register(get_user_model())

admin.site.register(Sale)
admin.site.register(Residential)
admin.site.register(Commercial)