from django.contrib import admin
from .models import Poll, Uservoted


# Register your models here.

admin.site.register(Poll)
admin.site.register(Uservoted)
