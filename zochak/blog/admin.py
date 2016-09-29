from django.contrib import admin
from .models import Zocbo


class Zocbo_Admin(admin.ModelAdmin):
    list_display = ["id", "name"]


admin.site.register(Zocbo, Zocbo_Admin)
