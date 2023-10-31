from django.contrib import admin
from .views import *
from .models import *


# Register your models here.

admin.site.register(About)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Contact)